from .cart import Cart


def cart_count(request):
    total_qty = 0
    try:
        cart_instance = Cart(request)

        total_qty = len(cart_instance)

    except Exception as e:

        total_qty = 0


    return {
        'ok': True,
        'cart_total_qty': total_qty,
    }
