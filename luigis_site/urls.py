from django.urls import path
from . import views

app_name = 'checkout'

urlpatterns = [
    path('', views.homePage, name='homepage'),
    path('menu/', views.menuPage, name='menu'),
    path('cart/', views.cartPage, name='cart'),
    path('checkout/', views.checkoutPage, name='checkout'),
    path('submit/', submit_checkout, name='submit_checkout'),
]
