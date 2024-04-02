
from django.db import models

class Ruta(models.Model):
    nombre_ruta = models.CharField(max_length=50)
    descripcion_ruta = models.TextField(blank=True, null=True)
    activo = models.BooleanField(default=True, blank=False, null=True)

    class Meta:
        db_table = 'rutas'
    
    