from django.urls import path

from . import views

app_name = "Apps.ventas"
urlpatterns = [
    path('', views.ListaVentasView, name='lista_ventas'),
    path('agregar', views.VistaAgregarVentas, name='agregar_ventas'),
    path('Abonar/<str:id_venta>/', views.AbonarTransaccion2, name='agregar_abono'),
    path('actualizar/<str:id_venta>/',
        views.VistaActulizarVenta, name='actualizar_venta'),
    path('eliminar/<str:id_venta>/',
        views.VistaEliminarVenta, name='eliminar_venta'),
    
    path('fcobros/', views.redireccion_fcobros, name='redireccion_fcobros'),

    #-----reportes---    
    path('report', views.VentasView, name='report'),
    path('reportC', views.ClientesView, name='reportC'),
    path('reportCT', views.ClientesCTView, name='reportCT'),
    path('reportS', views.ClientesSView, name='reportS'),
    
    path('generar_reporte_excel/<str:start_date>/<str:end_date>/', views.generar_reporte_excel, name='generar_reporte_excel'),
    path('generar_reporte_cliente_excel/<int:id_cliente>/', views.generar_reporte_cliente_excel, name='generar_reporte_cliente_excel'),
   
    path('generar_reporte_abonos_cliente/<str:start_date>/<str:end_date>/', views.generar_reporte_abonos_clientes_excel, name='generar_reporte_abonos_cliente'),

    # Nueva ruta para generar reporte en formato PDF y mostrar datos preliminares
    path('generar_reporte_pdf/<str:start_date>/<str:end_date>/', views.generar_reporte_pdf, name='generar_reporte_pdf'),
    path('generar_reporte_cliente_pdf/<int:id_cliente>/', views.generar_reporte_cliente_pdf, name='generar_reporte_cliente_pdf'),
    path('generar_reporte_abonos_cliente_pdf/<str:start_date>/<str:end_date>/', views.generar_reporte_abonos_clientes_pdf, name='generar_reporte_abonos_cliente_pdf'),
    path('obtener_datos_filtrados/<str:start_date>/<str:end_date>/', views.obtener_datos_filtrados, name='obtener_datos_filtrados'),


    path('obtener_datos_abonos_filtrados/<str:start_date>/<str:end_date>/', views.obtener_datos_abonos_filtrados, name='obtener_datos_abonos_filtrados'),
    path('obtener_datos_abonos_filtrados_id/<int:id_cliente>/', views.obtener_datos_abonos_filtrados_id, name='obtener_datos_abonos_filtrados_id'),



    path('VreportC', views.VentasCView, name='VreportC'),
    path('obtener_datos_filtrados_contado/<str:start_date>/<str:end_date>/', views.obtener_datos_filtrados_contado, name='obtener_datos_filtrados_contado'),
    path('generar_reporte_excel_contado/<str:start_date>/<str:end_date>/', views.generar_reporte_excel_contado, name='generar_reporte_excel_contado'),
    path('generar_reporte_pdf_contado/<str:start_date>/<str:end_date>/', views.generar_reporte_pdf_contado, name='generar_reporte_pdf_contado'),

    path('VreportCR', views.VentasCRView, name='VreportCR'),
    path('generar_reporte_excel_credito/<str:start_date>/<str:end_date>/', views.generar_reporte_excel_credito, name='generar_reporte_excel_credito'),
    path('generar_reporte_pdf_credito/<str:start_date>/<str:end_date>/', views.generar_reporte_pdf_credito, name='generar_reporte_pdf_credito'),
    path('obtener_datos_filtrados_credito/<str:start_date>/<str:end_date>/', views.obtener_datos_filtrados_credito, name='obtener_datos_filtrados_credito'),


    path('ventas/generar_reporte_saldos_clientes_excel/<int:id_cliente>/', views.generar_reporte_saldos_clientes_excel, name='generar_reporte_saldos_clientes_excel'),
    path('ventas/generar_reporte_saldos_clientes_pdf/<int:id_cliente>/', views.generar_reporte_saldos_clientes_pdf, name='generar_reporte_saldos_clientes_pdf'),
    path('obtener_datos_saldos_filtrados/<int:id_cliente>/', views.obtener_datos_saldos_filtrados, name='obtener_datos_saldos_filtrados'),
]
