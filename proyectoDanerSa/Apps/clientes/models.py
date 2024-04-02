from django.db import models
from decimal import Decimal
from Apps.rutas.models import Ruta

class Cliente(models.Model):
    nombre = models.CharField(max_length=256)
    direccion = models.TextField(max_length=256, blank=False, null=False)
    telefono = models.CharField(max_length=30, blank=False, null=False)
    saldo = models.DecimalField(max_digits=10, decimal_places=2, default=Decimal('0.00'), blank=False, null=True)
    activo = models.BooleanField(default=True, blank=False, null=True)
    ruta = models.ForeignKey(Ruta, on_delete=models.CASCADE, null=True)

    class Meta:
        db_table = 'clientes'
    
    def to_json(self):
        return {
            'id': self.id,
            'nombre': self.nombre,
            'saldo': self.saldo,
        }

class SaldoInicial(models.Model):
    cliente = models.OneToOneField(Cliente, on_delete=models.CASCADE, null=True)
    saldo_inicial = models.DecimalField(max_digits=15, decimal_places=2)
    abono_saldo = models.DecimalField(max_digits=15, decimal_places=2, default=0)
    estado = models.BooleanField(default=True, blank=False, null=True)

    class Meta: 
        db_table = 'saldoInicial'


class AbonoSaldoInicial(models.Model):
    id_saldo_inicial = models.ForeignKey(SaldoInicial, on_delete=models.CASCADE, null=True)
    fecha = models.DateField()
    monto_SI = models.DecimalField(max_digits=15, decimal_places=2)

    class Meta:
        db_table = 'abonosSaldoInicial'