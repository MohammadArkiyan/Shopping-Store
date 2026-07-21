from django.urls import path
from . import views

app_name = 'shop'
urlpatterns = [
    path('', views.product_list_view, name='shop'),
    path('detail/<int:pk>', views.product_detail, name='detail'),
    path('ajax/live-search/', views.live_search_view, name='live_search'),
]
