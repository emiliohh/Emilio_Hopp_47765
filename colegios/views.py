from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import *

@login_required
def agregarAvatar(request):
    if request.method=="POST":
        form = AvatarFormulario(request.POST, request.FILES)
        if form.is_valid():
            usuarioActual= User.objects.get(username=request.user)
            avatar = Avatar(usuario=usuarioActual, imagen=form.cleaned_data["imagen"])
            avatar.save()
            return render(request, "colegios/inicio.html")
    else:
        form = AvatarFormulario()
    return render(request,"colegios/agregarAvatar.html", {"form":form})     


def login_view(request):
    if request.method == "POST":
        form_inicio = AuthenticationForm(request,data = request.POST)
        if form_inicio.is_valid():
            info = form_inicio.cleaned_data
            usuario = info.get("username")
            contra = info.get("password")
            user  = authenticate(username=usuario,password=contra)
            if user:
                login(request, user)
                return render(request, "colegios/inicio.html", {"mensaje":f"Bienvenido {user}"})
        else:
            return render(request, "colegios/inicio.html",{"mensaje":"Datos incorrectos"})
    else: 
        form_inicio = AuthenticationForm()
    return render(request, "colegios/login.html", {"form":form_inicio})

def register(request):
    if request.method == 'POST':
            form = UsuarioRegistro(request.POST)
            #form = UserRegisterForm(request.POST)
            if form.is_valid():
                  username = form.cleaned_data['username']
                  form.save()
                  return render(request,"colegios/inicio.html", {"mensaje":"Usuario Creado :)"})
    else:
            form = UsuarioRegistro()       
            #form = UserRegisterForm()     
    return render(request,"colegios/registro.html" ,  {"form":form})

@login_required
def editarUsuario(request):
    usuario= request.user
    if request.method == "POST":
        form = FormularioEditar(request.POST)
        if form.is_valid():
            info= form.cleaned_data
            usuario.email = info["email"]
            usuario.set_password(info["password1"])
            usuario.first_name = info["first_name"]
            usuario.last_name = info["last_name"]
            usuario.save()
            return render(request, "colegios/inicio.html",  {"mensaje":"Usuario editado"})
    else:
        form= FormularioEditar(initial={
            "email":usuario.email,
            "first_name":usuario.first_name,
            "last_name":usuario.last_name,
        })
    return render(request,"colegios/editarPerfil.html",  {"form":form, "usuario":usuario})
            
def inicio(request):
    return render(request, "colegios/inicio.html")

def about(request):
    return render(request, "colegios/about.html")

@login_required
def buscar_colegio(request):
    return render(request, "colegios/buscar_colegio.html")

@login_required
def resultado_colegio(request):
    if request.GET["nombre"]:
        nombre = request.GET["nombre"]
        colegio_resultado = colegio.objects.filter(nombre__iexact=nombre)
        return render(request, "colegios/resultado_colegio.html", {"valor":nombre, "res":colegio_resultado})
    else:
        return HttpResponse("No enviaste datos")
        
    return render(request, "colegios/resultado_colegio.html")

#CRUD Becas

class becaLista(LoginRequiredMixin, ListView):
    model = beca
    
class becaCrear(LoginRequiredMixin, CreateView):
    model = beca
    fields = ["nombre", "descripcion"]
    success_url = "/colegios/becas/lista/"
    
class becaActualizar(LoginRequiredMixin, UpdateView):
    model = beca
    fields = ["nombre", "descripcion"]
    success_url = "/colegios/becas/lista/"
    
class becaBorrar(LoginRequiredMixin, DeleteView): 
    model = beca
    success_url = "/colegios/becas/lista/"
    
class becaDetalle(LoginRequiredMixin, DetailView):
    model = beca
    success_url = "/colegios/becas/lista/"

#CRUD Colegios

class colegioLista(LoginRequiredMixin, ListView):
    model = colegio
    
class colegioCrear(LoginRequiredMixin, CreateView):
    model = colegio
    fields = ["nombre","direccion","email","dependencia"]
    success_url = "/colegios/colegios/lista/"
    
class colegioActualizar(LoginRequiredMixin, UpdateView):
    model = colegio
    fields = ["nombre","direccion","email","dependencia"]
    success_url = "/colegios/colegios/lista/"
    
class colegioBorrar(LoginRequiredMixin, DeleteView): 
    model = colegio
    success_url = "/colegios/colegios/lista/"
    
class colegioDetalle(LoginRequiredMixin, DetailView):
    model = colegio
    success_url = "/colegios/colegios/lista/"
    

#CRUD Infra

class infraLista(LoginRequiredMixin, ListView):
    model = infra
    
class infraCrear(LoginRequiredMixin, CreateView):
    model = infra
    fields = ["nombre","descripcion","tamaño","tipo"]
    success_url = "/colegios/infras/lista/"
    
class infraActualizar(LoginRequiredMixin, UpdateView):
    model = infra
    fields = ["nombre","descripcion","tamaño","tipo"]
    success_url = "/colegios/infras/lista/"
    
class infraBorrar(LoginRequiredMixin, DeleteView): 
    model = infra
    success_url = "/colegios/infras/lista/"
    
class infraDetalle(LoginRequiredMixin, DetailView):
    model = infra
    success_url = "/colegios/infras/lista/"
    

#CRUD actividades

class actividadLista(LoginRequiredMixin, ListView):
    model = actividad_ep
    
class actividadCrear(LoginRequiredMixin, CreateView):
    model = actividad_ep
    fields = ["nombre","periodicidad","duracion"]
    success_url = "/colegios/actividades/lista/"
    
class actividadActualizar(LoginRequiredMixin, UpdateView):
    model = actividad_ep
    fields = ["nombre","periodicidad","duracion"]
    success_url = "/colegios/actividades/lista/"
    
class actividadBorrar(LoginRequiredMixin, DeleteView): 
    model = actividad_ep
    success_url = "/colegios/actividades/lista/"
    
class actividadDetalle(LoginRequiredMixin, DetailView):
    model = actividad_ep
    success_url = "/colegios/actividades/lista/"    