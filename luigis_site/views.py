from django.shortcuts import render
from .models import MenuItem, CartItem
from .forms import MenuForm, CartForm
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
    cartItems = []
    subtotal = 0.0
    redirectSite = "/menu/"
    for qty in request.GET.items():
        itemId =  str(qty[0]).split("_")[1]
        if qty[1] != "":
            redirectSite = ""
            form = CartForm(MenuItem.objects.filter(id=itemId))
            if form.is_valid():
                item = form.save(commit=False)         
                item.id = itemId
                item.name = MenuItem.objects.filter(id=itemId)[0].name
                item.description = MenuItem.objects.filter(id=itemId)[0].description
                item.price = MenuItem.objects.filter(id=itemId)[0].price
                item.quantity = int(qty[1])
                subtotal += item.price * item.quantity
                form.save()
                cartItems.append(item)   
            print(subtotal)
    if request.method == 'POST':
        for item in cartItems:
            print(item.id)
            if item.id == request.POST.get("itemId"):
                cartItems.remove(item)
    tax = subtotal * 0.07
    total = tax + subtotal
    return render(request, 'luigis_site/cart.html', {'cartItems': cartItems, 'subtotal': subtotal, 'tax': tax, 'total': total})

def checkoutPage(request):
    subtotal = round(float(request.GET.get("subtotal")),2)
    tax = round(float(request.GET.get("tax")),2)
    total = round(float(request.GET.get("total")),2)
    return render(request, 'luigis_site/checkout.html', {'subtotal': subtotal, 'tax': tax, 'total': total})


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
