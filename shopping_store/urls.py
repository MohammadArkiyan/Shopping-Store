from django.urls import path
from . import views


app_name = 'shopping_store'
urlpatterns = [
    # Home Page
    path('', views.index, name='index'),
]