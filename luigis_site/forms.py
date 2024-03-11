from django import forms
from .models import MenuItem,CartItem

class MenuForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(MenuForm, self).__init__(*args, **kwargs)
        self.fields['quantity'].label = ""
    class Meta:
        model = MenuItem
        fields = ('quantity',)

class CartForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(CartForm, self).__init__(*args, **kwargs)
    class Meta:
        model = CartItem
        fields = ()