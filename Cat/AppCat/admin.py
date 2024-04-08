from django.contrib import admin
from .models import *

# Register your models here.


class ClienteAdmin(admin.ModelAdmin):
    list_display = ["nombre","apellido","email","edad","direccion"]
    search_fields = ["nombre","apellido","email"]
    list_per_page = 20

class CompraAdmin(admin.ModelAdmin):
    list_display = ['fecha','producto','direccion','nombreFiesta','cliente']
    list_editable = []
    search_fields = ['cliente','nombreFiesta']
    list_filter = ['fecha']
    list_per_page = 10


class PresupuestoAdmin(admin.ModelAdmin):
    list_display = ["nombre","precio","productos","direccion","cliente"]
    search_fields = ["nombre","cliente"]
    list_filter = ["cliente"]
