from django.shortcuts import render
from .models import MenuItem, CartItem

# Create your views here.
def homePage(request):
    return render(request, 'luigis_site/homepage.html', {})

def menuPage(request):
    menuItems = MenuItem.objects.all().order_by('name')
    return render(request, 'luigis_site/menu.html', {'menuItems': menuItems})

def cartPage(request):
    cartItems = CartItem.objects.all().order_by('name')
    return render(request, 'luigis_site/cart.html', {'cartItems': cartItems})

def checkoutPage(request):
    return render(request, 'luigis_site/checkout.html', {})