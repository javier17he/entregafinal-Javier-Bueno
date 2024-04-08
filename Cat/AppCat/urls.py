from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name="home"),
    #Usuario
    path("login/", iniciar_sesion, name="iniciar_sesion"),
    path("logout/", cerrar_sesion, name="cerrar_sesion"),
    path("registro/", registro, name="registro"),
    path("edit/", editar_usuario, name="editar_usuario"),
    path("contra/", CambiarContra.as_view(), name="cambiar_contraseña"),
    #imagenes
    path("avatar/", agregar_avatar, name="add_avatar"),

    #clientes
    path('cliente/', ver_clientes, name="cliente"),
    path('agregar_cliente/', agregar_cliente, name="agregar_cliente"),
    path('editar_cliente/<id>', editar_cliente, name="editar_cliente"),
    path('eliminar_cliente/<int:id>/', eliminar_cliente, name='eliminar_cliente'),


    #compra
    path('ver_compra/', ver_compra, name="ver_compra"),
    path('compra/', crear_compra, name="crear_compra"),
    path('editar_compra/<id>', editar_compra, name="editar_compra"),
    path('eliminar_compra/<int:id>', eliminar_compra, name="eliminar_compra"),

    #presupuesto
    path('presupuesto/', presupuesto, name="presupuesto"),
    path('agregar_presupuesto/', agregar_presupuesto, name="agregar_presupuesto"),
    path('editar_presupuesto/<id>/', editar_presupuesto, name="editar_presupuesto"),
    path('eliminar_presupuesto/<int:id>/', eliminar_presupuesto, name="eliminar_presupuesto"),
]