from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', include('shopping_store.urls', namespace='shopping_store')),
    path('coupon', include('coupon.urls', namespace='coupon')),
    path('cart/', include('cart.urls', namespace='cart')),
    path('account/', include('account.urls', namespace='account')),
    path('shop/', include('product.urls', namespace='product')),
    path('checkout/', include('checkout.urls', namespace='checkout')),
    path('contact/', include('contact.urls', namespace='contact')),
    path('admin/', admin.site.urls),

]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)