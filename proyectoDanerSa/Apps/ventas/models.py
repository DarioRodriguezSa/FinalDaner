from django.db import models
from Apps.clientes.models import Cliente
from Apps.inventario.models import Producto
from django.utils import timezone
from django.db.models import Sum 
from django.contrib.auth.models import User
from datetime import timedelta

class Venta(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    fecha = models.DateField(default=timezone.now)
    id_clientes = models.ForeignKey(
        Cliente, models.DO_NOTHING, db_column='id_clientes')
    total = models.DecimalField(max_digits=15, decimal_places=2, default=0)
    anticipo = models.DecimalField(max_digits=15, decimal_places=2, default=0)
    estado_cuenta = models.BooleanField(default=True)
    comentario = models.CharField(max_length=256, blank=True, null=True)
    fecha_cobro = models.DateField(default=None, blank=True, null=True)  

    class Meta:
        db_table = 'Venta'
    
    def getSaldo(self):
        saldo = self.total - self.anticipo
        return saldo
    
    def get_suma_abonos(self):
        abonos_total = self.transacciones_venta.aggregate(Sum('abono'))['abono__sum']
        return abonos_total or 0
    

    


class DetalleVenta(models.Model):
    id_venta = models.ForeignKey(
        Venta, models.CASCADE, db_column='venta') 
    id_producto = models.ForeignKey(
        Producto, models.DO_NOTHING, db_column='producto')
    precio = models.DecimalField(max_digits=15, decimal_places=2)
    ganancia = models.DecimalField(max_digits=15, decimal_places=2, default=0)
    cantidad = models.IntegerField()

    class Meta:
        db_table = 'DetalleVenta'

    def getprecioCompraActual(self):
        precio_compra = self.precio - self.ganancia
        return precio_compra




class Transaccion(models.Model):
    fecha = models.DateField(default=timezone.now)
    id_cliente = models.ForeignKey(Cliente, models.DO_NOTHING, db_column='cliente')
    id_venta = models.ForeignKey(Venta, models.DO_NOTHING, related_name='transacciones_venta')
    abono = models.DecimalField(max_digits=15, decimal_places=2)
    saldo_venta = models.DecimalField(max_digits=15, decimal_places=2)
    saldo_cliente = models.DecimalField(max_digits=15, decimal_places=2)

    class Meta:
        db_table = 'Transaccion'

