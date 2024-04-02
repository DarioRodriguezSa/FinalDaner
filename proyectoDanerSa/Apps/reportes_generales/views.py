
# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from Apps.ventas.models import Venta, DetalleVenta
from django.db.models import Sum
from django.http import JsonResponse
from datetime import datetime



@login_required(login_url="/accounts/login/")
def general(request):
    # Definir las variables con valores predeterminados
    opcion = None
    fecha_dia = None
    fecha_inicio = None
    fecha_fin = None
    fecha_mes = None
    resultados = {}

    if request.method == 'POST':
        opcion = request.POST.get('fecha')

        # Validar según la opción seleccionada
        if opcion == 'dia':
            fecha_dia = request.POST.get('fecha_dia')

            # Si la fecha está en blanco, mostrar un mensaje de error
            if not fecha_dia:
                return render(request, 'reportes_generales/index.html', {'error': 'Por favor, seleccione una fecha para la opción "Día".'})

            # Validar el formato de la fecha
            try:
                datetime.strptime(fecha_dia, '%Y-%m-%d')
            except ValueError:
                return render(request, 'reportes_generales/index.html', {'error': 'Formato de fecha no válido. Utilice YYYY-MM-DD.'})

            ventas = Venta.objects.filter(fecha=fecha_dia)

        elif opcion == 'rango_fecha':
            fecha_inicio = request.POST.get('fecha_inicio')
            fecha_fin = request.POST.get('fecha_fin')

            # Si alguna de las fechas está en blanco, mostrar un mensaje de error
            if not fecha_inicio or not fecha_fin:
                return render(request, 'reportes_generales/index.html', {'error': 'Por favor, complete ambas fechas para la opción "Rango de Fecha".'})

            # Validar el formato de las fechas
            try:
                datetime.strptime(fecha_inicio, '%Y-%m-%d')
                datetime.strptime(fecha_fin, '%Y-%m-%d')
            except ValueError:
                return render(request, 'reportes_generales/index.html', {'error': 'Formato de fecha no válido. Utilice YYYY-MM-DD.'})

            # Resto del código para validar rango de fechas
            ventas = Venta.objects.filter(fecha__range=[fecha_inicio, fecha_fin])

        elif opcion == 'mes':
            fecha_mes = request.POST.get('fecha_mes')

            # Si la fecha está en blanco, mostrar un mensaje de error
            if not fecha_mes:
                return render(request, 'reportes_generales/index.html', {'error': 'Por favor, seleccione un mes y año para la opción "Mes".'})

            # Validar el formato del mes y año
            try:
                datetime.strptime(fecha_mes, '%Y-%m')
            except ValueError:
                return render(request, 'reportes_generales/index.html', {'error': 'Formato de fecha no válido. Utilice YYYY-MM.'})

            year, month = map(int, fecha_mes.split('-'))
            ventas = Venta.objects.filter(fecha__month=month, fecha__year=year)

        else:
            ventas = Venta.objects.all()

        for venta in ventas:
            detalles = DetalleVenta.objects.filter(id_venta=venta.id)
            total_ganancia = detalles.aggregate(Sum('ganancia'))['ganancia__sum'] or 0

            for detalle in detalles:
                nombre_producto = detalle.id_producto.nombre

                # Crear o actualizar el diccionario de resultados
                if nombre_producto not in resultados:
                    resultados[nombre_producto] = {
                        'nombre_producto': nombre_producto,
                        'cantidad_total_producto': detalle.cantidad,
                        'cantidad_total_precio_venta': float(detalle.precio * detalle.cantidad),  # Convertir a float
                        'total_ganancia': total_ganancia,
                    }
                else:
                    resultados[nombre_producto]['cantidad_total_producto'] += detalle.cantidad
                    resultados[nombre_producto]['cantidad_total_precio_venta'] += float(detalle.precio * detalle.cantidad)  # Convertir a float
                    resultados[nombre_producto]['total_ganancia'] += total_ganancia

        # Inicializar resultados_chartjs
        resultados_chartjs = {'labels': [], 'data': {'cantidad_total_precio_venta': [], 'cantidad_total_producto': [], 'total_ganancia': []}}

        if resultados:
            resultados_chartjs = {
                'labels': list(resultados.keys()),
                'data': {
                    'cantidad_total_precio_venta': [float(item['cantidad_total_precio_venta']) for item in resultados.values()],
                    'cantidad_total_producto': [item['cantidad_total_producto'] for item in resultados.values()],
                    'total_ganancia': [float(item['total_ganancia'] )for item in resultados.values()]
                }
            }

        chart_data = {'resultados': list(resultados.values()), 'chartjs_data': resultados_chartjs}

        if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
            # Devolver JSON si es una solicitud AJAX (POST)
            return JsonResponse(chart_data, safe=False)

        # Esta parte se ejecutará si la solicitud no es AJAX
        return render(request, 'reportes_generales/index.html', {'chart_data': chart_data, 'opcion': opcion, 'fecha_dia': fecha_dia, 'fecha_inicio': fecha_inicio, 'fecha_fin': fecha_fin, 'fecha_mes': fecha_mes, 'error': None})

    # Esta parte se ejecutará si la solicitud es un GET
    return render(request, "reportes_generales/index.html", {'chart_data': None, 'opcion': None, 'fecha_dia': None, 'fecha_inicio': None, 'fecha_fin': None, 'fecha_mes': None, 'error': None})