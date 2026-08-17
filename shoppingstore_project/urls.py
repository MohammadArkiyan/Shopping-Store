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


# Media is always served by Django here since this project has no separate
# reverse proxy (e.g. nginx) in front of it. Static files are handled by
# WhiteNoise instead (see MIDDLEWARE / STORAGES in settings.py).
if not settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)