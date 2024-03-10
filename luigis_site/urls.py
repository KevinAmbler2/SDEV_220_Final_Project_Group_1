from django.urls import path
from . import views

urlpatterns = [
    path('', views.homePage, name='homepage'),
    path('menu/', views.menuPage, name='menu'),
    path('cart/', views.cartPage, name='cart'),
    path('checkout/', views.checkoutPage, name='checkout'),
]