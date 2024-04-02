from django.db import models
from decimal import Decimal

class Producto(models.Model):
    ACTIVO = 1
    INACTIVO = 0

    ESTADO_CHOICES = [
        (ACTIVO, 'Activo'),
        (INACTIVO, 'Inactivo'),
    ]

    idproducto = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=70)
    existencia = models.DecimalField(max_digits=10, decimal_places=2)
    precio_venta = models.DecimalField(max_digits=10, decimal_places=2)
    precio_compra = models.DecimalField(max_digits=10, decimal_places=2)
    estado = models.IntegerField(choices=ESTADO_CHOICES, default=ACTIVO)

    def __str__(self):
        return self.nombre
