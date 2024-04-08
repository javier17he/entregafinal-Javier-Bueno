from django import forms
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,UserChangeForm

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = '__all__'

class CompraForm(forms.ModelForm):
    class Meta:
        model = Compra
        fields = '__all__'

class presupuestoForm(forms.ModelForm):
    class Meta:
        model = presupuesto
        fields = '__all__'

class EditarClienteForm(UserChangeForm):

    password = None

    class Meta:
        model = User
        fields = ["first_name", "last_name",  "email"]
class RegistroUsuario(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','first_name','last_name','password1','password2']

class EditarUsuario(UserChangeForm):
    password = None
    class Meta:
        model = User
        fields = ["email","first_name","last_name"]
        widgets = {
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Correo electrónico'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Apellido'}),
        }
class AvatarFormulario(forms.Form):
    imagen = forms.ImageField()