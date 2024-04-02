from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Ruta
from django.contrib import messages

@login_required(login_url="/accounts/login/")
def ListaRutasView(request):
    context = {
        "rutas": Ruta.objects.filter(activo=True),
    }
    return render(request, "rutas/rutas.html", context=context)



@login_required(login_url="/accounts/login/")
def VistaAgregarRuta(request):
    if request.method == 'POST':
        data = request.POST
        attributes = {
            "nombre_ruta": data['nombreRuta'],
            "descripcion_ruta": data['descripcion'],
        }
        if Ruta.objects.filter(**attributes).exists():
            messages.error(request, '¡La ruta ya existe!',
                extra_tags="warning")
            return redirect('Apps.rutas:agregar_rutas')
        try:
            new_ruta = Ruta.objects.create(**attributes)
            new_ruta.save()
            messages.success(request, '¡Ruta: ' + attributes["nombre_ruta"] + " " + ' Creada con éxito!', extra_tags="success")
            return redirect('Apps.rutas:lista_rutas')
        except Exception as e:
            messages.success(
                request, f'Error en la creacion: {str(e)}',extra_tags="danger")
            return redirect('Apps.rutas:agregar_rutas')
    return render(request, "rutas/agregar_rutas.html")   


@login_required(login_url="/accounts/login/")
def VistaEliminarRuta(request, id_ruta):
    try:
        ruta = Ruta.objects.get(id=id_ruta)
        ruta.activo = False
        ruta.save()
        messages.success(request, '¡Ruta: ' + ruta.nombre_ruta +
            ' Eliminada!', extra_tags="success")
        return redirect('Apps.rutas:lista_rutas')
    except Exception as e:
        messages.success(
            request, '¡Hubo un error durante la eliminación!', extra_tags="danger")
        return redirect('Apps.rutas:lista_rutas')
    
@login_required(login_url="/accounts/login/")
def VistaActulizarRuta(request, id_ruta):
    try:
        ruta = Ruta.objects.get(pk=id_ruta)
    except Exception as e:
        messages.success(
            request, '¡Hubo un error al intentar localizar la ruta!', extra_tags="danger")
        return redirect('Apps.rutas:lista_rutas')
    context = {
        "rutas": ruta,
    }
    if request.method == 'POST':
        try:
            data = request.POST
            attributes = {
                "nombre_ruta": data['nombreRuta'],
                "descripcion_ruta": data['descripcion'],
            }
            ruta = Ruta.objects.filter(
                pk=id_ruta).update(**attributes)
            ruta = Ruta.objects.get(pk=id_ruta)
            messages.success(request, '¡Ruta: ' + ruta.nombre_ruta +
                ' actualizada exitosamente!', extra_tags="success")
            return redirect('Apps.rutas:lista_rutas')
        except Exception as e:
            messages.success(
                request, '¡Hubo un error durante la actualización!', extra_tags="danger")
            return redirect('Apps.rutas:lista_rutas')
    return render(request, "rutas/rutas.html", context=context)
