from django.urls import path

from . import views

app_name = "Apps.pos"
urlpatterns = [
  
    path('', views.ListaVentasgraph, name='lista_ventas_graph'),
]
