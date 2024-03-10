from django.shortcuts import render
from .models import MenuItem, CartItem
from .forms import MenuForm
from django.shortcuts import redirect

# Create your views here.
def homePage(request):
    return render(request, 'luigis_site/homepage.html', {})

def menuPage(request):
    menuItems = MenuItem.objects.all().order_by('id')
#    if request.method == "POST":
#        form = MenuForm(request.POST)
#        if form.is_valid():
#            item = form.save(commit=False)         
#            item.price = menuItems.filter(id=form.id)[0].price
#            item.save()
#            print(item)
#    else:
#        form = MenuForm()
#    form = MenuForm()
#    return render(request, 'luigis_site/menu.html', {'menuItems': menuItems,'form': form})
    return render(request, 'luigis_site/menu.html', {'menuItems': menuItems})

def cartPage(request):
    cartItems = CartItem.objects.all().order_by('id')
    return render(request, 'luigis_site/cart.html', {'cartItems': cartItems})

def checkoutPage(request):
    cartItems = CartItem.objects.all()
    return render(request, 'luigis_site/checkout.html', {'cartItems': cartItems})

def submit_checkout(request):
    if request.method == 'POST':
        first_name = request.POST.get('myFName')
        last_name = request.POST.get('myLName')
        credit_card = request.POST.get('myCreditCard')
        total = ('x') # replace with the calculate total function

        current_time = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        filename = f"checkout_{current_time}.txt"
        with open(filename, 'w') as file:
            file.write(f"First Name: {first_name}\n")
            file.write(f"Last Name: {last_name}\n")
            file.write(f"Credit Card: {credit_card}\n")
            file.write(f"Total: {total}\n")

        return render(request, 'luigis_site/confirmed.html')
    else:
        return render(request, 'luigis_site/checkout.html')
