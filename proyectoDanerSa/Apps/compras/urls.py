# urls.py
from django.urls import path
from . import views

app_name = "Apps.compras"
urlpatterns = [
    path('', views.sales_list_view, name='compras'),
    path('realizar_compra/', views.show_realizar_compra, name='realizar_compra'),
    path('realizar_compra/submit/', views.realizar_compra, name='realizar_compra_submit'),
    path('agregar_producto_desde_modal/', views.agregar_producto_desde_modal, name='agregar_producto_desde_modal'),


    path('Creport', views.ComprasView, name='reportCo'),
    path('generar_reporte_excel_compras/<str:start_date>/<str:end_date>/', views.generar_reporte_compras_excel, name='generar_reporte_excel_compras'),
    path('generar_reporte_pdf_compras/<str:start_date>/<str:end_date>/', views.generar_reporte_compras_pdf, name='generar_reporte_pdf_compras'),
    path('obtener_datos_filtrados_compras/<str:start_date>/<str:end_date>/', views.obtener_datos_filtrados_compras, name='obtener_datos_filtrados_compras'),

]
