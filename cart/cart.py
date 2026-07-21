from decimal import Decimal
from django.db.models import Sum
from product.models import Product
from .models import Cart as CartModel, CartItem
from coupon.models import Coupon


class Cart:
    def __init__(self, request):
        self.request = request
        self.session = request.session
        self.db_cart = None  # cart db object
        cart = self.session.get('cart')  # cart session dictionary

        # DataBase
        if self.request.user.is_authenticated:
            self.db_cart, created = CartModel.objects.get_or_create(
                user=self.request.user
            )

            session_cart_data = self.session.get('cart')
            if session_cart_data and len(session_cart_data) > 0:
                for product_id, item_data in session_cart_data.items():
                    try:
                        product = Product.objects.get(id=product_id)

                    except Product.DoesNotExist:
                        continue

                    quantity = item_data['quantity']
                    price_snapshot = item_data['price']

                    cart_item, created = CartItem.objects.get_or_create(
                        cart=self.db_cart,
                        product=product,

                        defaults={
                            'quantity': quantity,
                            'price': Decimal(str(price_snapshot)),
                        }
                    )

                    if not created:
                        cart_item.quantity += quantity
                        cart_item.save()

                del self.session['cart']
                self.session.modified = True
        # Session
        else:
            if not cart:
                cart = {}
                self.session['cart'] = cart

            self.cart = cart
        self.coupon_id = self.session.get('coupon_id')

    def add(self, product, quantity=1):

        price_snapshot = product.price

        if self.request.user.is_authenticated:
            cart_item, created = CartItem.objects.get_or_create(
                cart=self.db_cart,
                product=product,
                defaults={'quantity': quantity, 'price': price_snapshot}

            )
            if not created:
                cart_item.quantity += quantity
                cart_item.save()
        else:
            product_id = str(product.id)
            if product_id not in self.cart:
                self.cart[product_id] = {'quantity': 0, 'price': str(product.price)}
            self.cart[product_id]['quantity'] += quantity

            self.save()

    def decrement(self, product, quantity=1):
        if self.request.user.is_authenticated:
            try:
                cart_item = CartItem.objects.get(cart=self.db_cart, product=product)
                cart_item.quantity -= quantity

                if cart_item.quantity <= 0:
                    cart_item.delete()
                else:
                    cart_item.save()
            except CartItem.DoesNotExist:
                pass

        else:
            product_id = str(product.id)

            if product_id in self.cart:
                self.cart[product_id]['quantity'] -= quantity

            if self.cart[product_id]['quantity'] <= 0:
                del self.cart[product_id]

            self.save()

    def remove(self, product):
        if self.request.user.is_authenticated:
            try:
                cart_item = CartItem.objects.get(cart=self.db_cart, product=product)
                cart_item.delete()

            except CartItem.DoesNotExist:
                pass

        else:
            product_id = str(product.id)

            if product_id in self.cart:
                del self.cart[product_id]

            self.save()

    def get_total_price(self):
        if self.request.user.is_authenticated:
            # 💡 اصلاح: اطمینان از برگشت Decimal و مدیریت None
            total = self.db_cart.get_total_price
            return Decimal(str(total)) if total is not None else Decimal('0')
        else:
            return sum(Decimal(item['price']) * item['quantity'] for item in self.cart.values())

    def get_final_price(self):
        total = self.get_total_price()
        discount = self.get_discount()
        shipping_cost = Decimal('10000')

        return (total - discount) + shipping_cost

    def get_item(self, product_id):
        product_id = int(product_id)
        if self.request.user.is_authenticated:

            try:

                item = self.db_cart.items.get(product__id=product_id)

                return {
                    'product_id': item.product.id,
                    'quantity': item.quantity,
                    'price': str(item.price),
                    'line_total': str(item.line_total),
                }
            except CartItem.DoesNotExist:
                return None
        else:

            product_id_str = str(product_id)
            if product_id_str in self.cart:
                return {
                    'product_id': product_id,
                    'quantity': self.cart[product_id_str]['quantity'],

                    'price': self.cart[product_id_str]['price'],

                    'line_total': str(
                        Decimal(self.cart[product_id_str]['price']) * self.cart[product_id_str]['quantity']
                    ),
                }
            return None

    def save(self):

        if self.coupon_id:
            self.session['coupon_id'] = self.coupon_id
        elif 'coupon_id' in self.session:
            del self.session['coupon_id']

        self.session.modified = True

    @property
    def coupon(self):
        if self.coupon_id:
            try:
                return Coupon.objects.get(id=self.coupon_id)
            except Coupon.DoesNotExist:
                return None
        return None

    def get_discount(self):

        if self.coupon:
            return self.get_total_price() * (self.coupon.discount / Decimal('100'))
        return Decimal('0')

    def __iter__(self):
        if self.request.user.is_authenticated:
            items = self.db_cart.items.select_related('product').all()
            for item in items:
                yield {
                    'product': item.product,
                    'quantity': item.quantity,
                    'price': item.price,
                    'total_price': item.line_total

                }
        else:

            product_ids = self.cart.keys()

            products = Product.objects.filter(id__in=product_ids)

            cart = self.cart.copy()

            for product in products:
                item = cart[str(product.id)]
                item['product'] = product

                item['total_price'] = Decimal(item['price']) * item['quantity']

                yield item

    def __len__(self):
        if self.request.user.is_authenticated:
            return self.db_cart.items.aggregate(count=Sum('quantity'))['count'] or 0
        else:
            return sum(item['quantity'] for item in self.cart.values())
