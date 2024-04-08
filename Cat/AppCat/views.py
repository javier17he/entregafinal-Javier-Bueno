from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import *
from django.contrib import messages
from django.core.paginator import Paginator
from django.http import Http404
#contrib.auth
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.views import PasswordChangeView
#LoginRequired
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.

#INICIAR SESION
def iniciar_sesion(request):
    if request.method == "POST":
        formulario = AuthenticationForm(request, data=request.POST)
        if formulario.is_valid():
            info_dict = formulario.cleaned_data
            usuario = authenticate(username=info_dict["username"],password=info_dict["password"])
            if usuario:
                login(request,usuario)
                messages.success(request, "Sesion Iniciada")
                return redirect(to="home")
        else:
            return render(request, "AppCat/home.html")
    
    else:
        formulario = AuthenticationForm()
    
    return render(request, "AppCat/registro/inicio_sesion.html", {'form':formulario})

#CERRAR SESION
@login_required
def cerrar_sesion(request):
    logout(request)
    messages.success(request, "Sesion Finalizada")
    return redirect(to="home")

#REGISTRARSE
def registro(request):
    data = {
        'form': RegistroUsuario()
    }

    if request.method == "POST":
        formulario = RegistroUsuario(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            user = authenticate(username=formulario.cleaned_data["username"],
                                password=formulario.cleaned_data["password1"])
            login(request, user)
            messages.success(request, "Te has registrado correctamente")
            return redirect(to='home')
        else:
            data['form'] = formulario
    
    return render(request, "AppCat/registro/registro.html", data)

#UPDATE
@login_required
def editar_usuario(request):
    usuario = request.user
    if request.method == "POST":
        formulario = EditarUsuario(request.POST)
        if formulario.is_valid():
            info = formulario.cleaned_data
            usuario.email = info["email"]
            usuario.first_name = info["first_name"]
            usuario.last_name = info["last_name"]
            usuario.save()
            messages.success(request, "Cambios Guardados")
            return redirect(to="home")
    else:
        formulario = EditarUsuario()
    return render(request, "AppCat/registro/editar_usuario.html", {"form":formulario})

#CAMBIAR CONTRASEÑA
class CambiarContra(LoginRequiredMixin, PasswordChangeView):
    template_name = "AppCat/registro/cambiar_contra.html"
    success_url = "/AppCat/"

#AVATAR
@login_required
def agregar_avatar(request):
    if request.method == "POST":
        formulario = AvatarFormulario(request.POST, request.FILES)
        if formulario.is_valid():
            info = formulario.cleaned_data
            usuario_actual = User.objects.get(username=request.user)
            nuevo_avatar = Avatar(usuario=usuario_actual,imagen=info["imagen"])
            nuevo_avatar.save()
            messages.success(request, "Avatar Cambiado")
            return redirect(to="home")
    else:
        formulario = AvatarFormulario()
    
    return render(request, "AppCat/registro/nuevo_avatar.html", {"form":formulario})

#INICIO
def home(request):
    return render(request, "AppCat/home.html")

#CLIENTES
#CREAR
@login_required
def agregar_cliente(request):
    data = {
        'form':ClienteForm()
    }

    if request.method == "POST":
        formulario =ClienteForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Cliente creado")
            return redirect(to="cliente")
        else:
            data['form'] = formulario
            
    return render(request, 'AppCat/cliente/agregar.html', data)

#VER
@login_required
def ver_clientes(request):
    cliente = Cliente.objects.all()
    page = request.GET.get('page', 1)

    try:
        paginator = Paginator(cliente, 8)
        cliente = paginator.page(page)
    except:
        raise Http404

    data = {
        'entity':cliente,
        'paginator': paginator
    }

    return render(request, 'AppCat/cliente/ver.html', data)

#UPDATE
@login_required
def editar_cliente(request,id):
    cliente = get_object_or_404(Cliente, id=id)
    data = {
        'form':ClienteForm(instance=cliente)
    }

    if request.method == "POST":
        formulario = ClienteForm(data=request.POST, instance=cliente)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Cliente modificado correctamente")
            return redirect(to="cliente")
        else:
            data['form'] = formulario

    return render(request, "AppCat/cliente/modificar.html", data)

#Eliminar
@login_required
def eliminar_cliente(request, id):
    cliente = get_object_or_404(Cliente, id=id)
    cliente.delete()
    messages.success(request, "Cliente eliminado")
    return redirect("cliente")

#COMPRA
#CREAR
def crear_compra(request):
    data = {
        'form': CompraForm()
    }

    if request.method == "POST":
        formulario = CompraForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Compra creada")
            return redirect(to="crear_compra")
        else:
            data['form'] = formulario
            
    return render(request, 'AppCat/compra.html', data)

#Ver
@login_required
def ver_compra(request):
    consulta = Compra.objects.all()
    page = request.GET.get('page', 1)

    try:
        paginator = Paginator(consulta, 8)
        consulta = paginator.page(page)
    except:
        raise Http404

    data = {
        'entity': consulta,
        'paginator': paginator
    }

    return render(request, 'AppAlvar/compra/ver.html', data)


#UPDATE
@login_required
def editar_compra(request,id):
    consulta = get_object_or_404(Compra, id=id)
    data = {
        'form': CompraForm(instance=consulta)
    }

    if request.method == "POST":
        formulario = CompraForm(data=request.POST, instance=consulta)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Modificado correctamente")
            return redirect(to="ver_consulta")
        else:
            data['form'] = formulario

    return render(request, "AppAlvar/compra/modificar.html", data)


#Eliminar
@login_required
def eliminar_compra(request,id):
    constulta = get_object_or_404(Compra, id=id)
    constulta.delete()
    messages.success(request, "Compra eliminada correctamente")
    return redirect(to="ver_compra")

#Prsupuesto
#Crear
@login_required
def agregar_presupuesto(request):
    data = {
        'form': presupuestoForm()
    }

    if request.method == "POST":
        formulario = presupuestoForm(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Presupuesto Creado")
            return redirect(to="presupuesto")
        else:
            data['form'] = formulario

    return render(request, "AppCat/presupuesto/agregar.html", data)


#Ver
def presupuesto(request):
    proyectos = presupuesto.objects.all()
    page = request.GET.get('page', 1)

    try:
        paginator = Paginator(presupuesto, 8)
        presupuesto = paginator.page(page)
    except:
        raise Http404

    data = {
        'entity': presupuesto,
        'paginator': paginator
    }

    return render(request, 'AppCat/presupuesto.html', data)


#UPDATE
@login_required
def editar_presupuesto(request,id):
    presupuesto = get_object_or_404(presupuesto, id=id)
    data = {
        'form': presupuestoForm(instance=presupuesto)
    }

    if request.method == "POST":
        formulario = presupuestoForm(data=request.POST, instance=presupuesto, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Presupuesto modificado correctamente")
            return redirect(to="presupuesto")
        else:
            data['form'] = formulario

    return render(request, "AppCat/presupuesto/modificar.html", data)


#Eliminar
@login_required
def eliminar_presupuesto(request,id):
    presupuesto = get_object_or_404(presupuesto, id=id)
    presupuesto.delete()
    messages.success(request, "Presupuesto eliminado correctamente")
    return redirect(to="presupuesto")
