from django.urls import path

from . import views

app_name = "Apps.clientes"
urlpatterns = [
    path('', views.ListaClientesView, name='lista_clientes'),
    path('agregar', views.VistaAgregarCliente, name='agregar_cliente'),
    path('actualizar/<str:id_cliente>/',
        views.VistaActulizarCliente, name='actualizar_cliente'),
    path('eliminar/<str:id_cliente>/',
        views.VistaEliminarCliente, name='eliminar_cliente'),
    path('saldar/<str:id_cliente>/',
        views.VistaPagarSaldo, name='saldar_cliente'),
    path('detalles/<str:id_cliente>/',
        views.DetalleClientesView, name='detalles_clientes'),
    path("get", views.GetClientsAJAXView, name="get_clientes"),




    path('report', views.VistaCliente, name='VistaCliente'),
    path('clireport', views.ClienteView, name='reportcli'),
    path('generar_reporte_excel_saldos/', views.generar_reporte_clientes_excel, name='generar_reporte_excel_saldos'),
    path('generar_reporte_pdf_saldos/', views.generar_reporte_clientes_pdf, name='generar_reporte_pdf_saldos'),
    path('obtener_datos_filtrados_clientes/', views.obtener_datos_filtrados_clientes, name='obtener_datos_filtrados_clientes'),
]

