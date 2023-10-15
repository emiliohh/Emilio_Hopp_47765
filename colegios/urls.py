from django.urls import path
from .views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path("inicio/", inicio, name="Inicio"),
    path("about/", about, name="about"),
    path("buscar_colegio/", buscar_colegio, name="BuscarColegio"),
    path("resu_colegio/", resultado_colegio, name="ResultadoColegio"),
    path("login/", login_view, name="Login"),
    path("register/", register , name="Registro"),
    path("logout",LogoutView.as_view(template_name="colegios/logout.html"), name="Logout"),
    path("editar/",editarUsuario, name="EditarUsuario"),
    path("agregar/",agregarAvatar, name="Avatar"),
    #colegios
    path("colegios/lista/", colegioLista.as_view(), name="lista_colegios"),
    path("colegios/nuevo/", colegioCrear.as_view(), name="crear_colegio"),
    path("colegios/actualizar/<int:pk>", colegioActualizar.as_view(), name="Actualizar colegio"),
    path("colegios/borrar/<int:pk>", colegioBorrar.as_view(), name="Borrar colegio"),
    path("colegios/detalle/<int:pk>", colegioDetalle.as_view(), name="Detalle colegio"),
    #becas
    path("becas/lista/", becaLista.as_view(), name="lista_becas"),
    path("becas/nueva/", becaCrear.as_view(), name="crear_beca"),
    path("becas/actualizar/<int:pk>", becaActualizar.as_view(), name="Actualizar beca"),
    path("becas/borrar/<int:pk>", becaBorrar.as_view(), name="Borrar beca"),
    path("becas/detalle/<int:pk>", becaDetalle.as_view(), name="Detalle beca"),
    #infra
    path("infras/lista/", infraLista.as_view(), name="lista_infras"),
    path("infras/nueva/", infraCrear.as_view(), name="crear_infra"),
    path("infras/actualizar/<int:pk>", infraActualizar.as_view(), name="Actualizar infra"),
    path("infras/borrar/<int:pk>", infraBorrar.as_view(), name="Borrar infra"),
    path("infras/detalle/<int:pk>", infraDetalle.as_view(), name="Detalle infra"),
    #actividades
    path("actividades/lista/", actividadLista.as_view(), name="lista_actividades"),
    path("actividades/nueva/", actividadCrear.as_view(), name="crear_actividad"),
    path("actividades/actualizar/<int:pk>", actividadActualizar.as_view(), name="Actualizar actividad"),
    path("actividades/borrar/<int:pk>", actividadBorrar.as_view(), name="Borrar actividad"),
    path("actividades/detalle/<int:pk>", actividadDetalle.as_view(), name="Detalle actividad"),
]