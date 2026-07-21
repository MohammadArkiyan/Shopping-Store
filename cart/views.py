from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from .cart import Cart
from product.models import Product


def cart_detail(request):
    cart = Cart(request)

    coupon_error = request.session.pop('coupon_error', None)
    context = {
        'cart': cart,
        'coupon_error': coupon_error,
    }

    return render(request, 'cart/cart.html', context)


def cart_add(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    quantity = int(request.POST.get('quantity', 1))

    cart.add(product=product, quantity=quantity)
    return _cart_snapshot(cart, product)


def cart_decrement(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.decrement(product=product, quantity=1)
    return _cart_snapshot(cart, product)


def cart_remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product=product)

    return _cart_snapshot(cart, product, removed=True)


def _cart_snapshot(cart, product=None, removed=False):
    payload = {
        'ok': True,
        'total_qty': len(cart),
        'subtotal': str(cart.get_total_price()),
        'final_total': str(cart.get_final_price()),
        'item': None
    }

    if product and not removed:

        item_data = cart.get_item(product.id)

        if item_data:
            payload['item'] = item_data
        else:
            payload['item'] = None


    return JsonResponse(payload)
