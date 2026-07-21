from django.shortcuts import redirect
from django.utils import timezone
from django.views.decorators.http import require_POST
from .models import Coupon
from cart.cart import Cart


@require_POST
def coupon_apply(request):
    now = timezone.now()

    code = request.POST.get('code')

    if code:
        try:

            coupon = Coupon.objects.get(
                code__iexact=code,
                valid_from__lte=now,
                valid_to__gte=now,
                active=True
            )

            cart = Cart(request)
            cart.coupon_id = coupon.id
            cart.save()

        except Coupon.DoesNotExist:

            request.session['coupon_error'] = 'The coupon code is invalid or expired.'

    return redirect('cart:detail')


def coupon_remove(request):
    cart = Cart(request)
    if 'coupon_id' in cart.session:
        del cart.session['coupon_id']
        cart.save()

    return redirect('cart:detail')
