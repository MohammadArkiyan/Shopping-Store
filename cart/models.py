from decimal import Decimal
from django.db.models import Sum, F
from django.db import models
from django.conf import settings
from product.models import Product


class Cart(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    @property
    def get_total_price(self):

        total = self.items.aggregate(
            cart_total = Sum(F('price') * F('quantity'))
        )
        return total['cart_total'] or Decimal(0)

    @property
    def get_final_price(self):

        shipping_cost = Decimal('10.00')
        return self.get_total_price + shipping_cost

    def __str__(self):
        return f"Cart of {self.user.username or self.user.id}"




class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    @property
    def line_total(self):
        return  self.price * self.quantity

    def __str__(self):
        return f"{self.price} * {self.quantity} in Cart {self.cart.id}"



