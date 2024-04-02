from django.urls import path

from . import views

app_name = "Apps.rutas"
urlpatterns = [
    path('', views.ListaRutasView, name='lista_rutas'),
    path('agregar', views.VistaAgregarRuta, name='agregar_rutas'),
    path('eliminar/<str:id_ruta>/',
        views.VistaEliminarRuta, name='eliminar_ruta'),
    path('actualizar/<str:id_ruta>/',
        views.VistaActulizarRuta, name='actualizar_ruta'),
]

