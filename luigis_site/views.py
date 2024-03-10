from django.shortcuts import render
from .models import MenuItem, CartItem
from .forms import MenuForm
from django.shortcuts import redirect

# Create your views here.
def homePage(request):
    return render(request, 'luigis_site/homepage.html', {})

def menuPage(request):
    menuItems = MenuItem.objects.all().order_by('name')
#    if request.method == "POST":
#        form = MenuForm(request.POST)
#        if form.is_valid():
#            post = form.save(commit=False)
#            post.save()
#    else:
#        form = MenuForm()
    form = MenuForm()
    return render(request, 'luigis_site/menu.html', {'menuItems': menuItems,'form': form})

def cartPage(request):
    cartItems = CartItem.objects.all().order_by('name')
    return render(request, 'luigis_site/cart.html', {'cartItems': cartItems})

def checkoutPage(request):
    cartItems = CartItem.objects.all()
    return render(request, 'luigis_site/checkout.html', {'cartItems': cartItems})