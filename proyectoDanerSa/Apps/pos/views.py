from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from Apps.ventas.models import DetalleVenta
from django.db.models import Sum
from datetime import datetime, timedelta
from django.utils import timezone
from django.db.models import F

@login_required(login_url="/accounts/login/")
def ListaVentasgraph(request):
    fecha_actual = timezone.now()

    inicio_semana = fecha_actual - timedelta(days=fecha_actual.weekday())
    fin_semana = inicio_semana + timedelta(days=6)

    ventas_por_producto = DetalleVenta.objects.filter(
        id_venta__fecha__range=(inicio_semana, fecha_actual)
    ).annotate(
        nombre_producto=F('id_producto__nombre')
    ).values('nombre_producto').annotate(
        total_ventas=Sum('cantidad')
    )

    productos = []
    ventas_totales = []

    for venta in ventas_por_producto:
        productos.append(venta['nombre_producto'])
        ventas_totales.append(venta['total_ventas'])

    data = {
        'productos': productos,
        'ventas_totales': ventas_totales,
        'inicio_semana': inicio_semana.strftime('%Y-%m-%d'),
        'fin_semana': fin_semana.strftime('%Y-%m-%d'),
    }

    return render(request, 'pos/grafica.html', data)
