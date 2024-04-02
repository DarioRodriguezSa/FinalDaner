from django.urls import path
from . import views

app_name = "Apps.inventario"
urlpatterns = [
    path('', views.index, name='index'),  # Agrega esta línea para la vista 'index'
    path('agregar', views.VistaAgregarProducto, name='agregar_producto'),
    path('modificar/<int:producto_id>/', views.modificar_producto, name='modificar_producto'),
    path('eliminar/<int:producto_id>/', views.eliminar_producto, name='eliminar_producto'),
    # Agrega otras rutas según sea necesario




     path('Ireport', views.InventarioView, name='reportI'),
     path('generar_reporte_excel_inventario/', views.generar_reporte_inventario_excel, name='generar_reporte_excel_inventario'),
     path('generar_reporte_pdf_inventario/', views.generar_reporte_inventario_pdf, name='generar_reporte_pdf_inventario'),
     path('obtener_datos_filtrados_inventario/', views.obtener_datos_filtrados_inventario, name='obtener_datos_filtrados_inventario'),

]
