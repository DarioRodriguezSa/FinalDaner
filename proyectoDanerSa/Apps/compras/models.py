from django.db import models
from Apps.inventario.models import Producto
from decimal import Decimal

class Compra(models.Model):
    idcompra = models.AutoField(primary_key=True)
    fecha = models.DateField(auto_now_add=True)
    costo_compra = models.DecimalField(max_digits=10, decimal_places=2)
    cantidad = models.DecimalField(max_digits=10, decimal_places=2)
    observaciones = models.CharField(max_length=200, null=True)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('idcompra', 'producto')

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)  # Llama al método save original para guardar la compra
        existencia_anterior = self.producto.existencia - self.cantidad
        costo_compra_anterior = self.producto.precio_compra * existencia_anterior
        costo_compra_actual = self.costo_compra * self.cantidad
        # Calcular el nuevo costo total antes de dividir
        nuevo_costo_total = costo_compra_anterior + costo_compra_actual
        # actualizar existencia antes de calcular el nuevo costo promedio
        nueva_existencia = self.producto.existencia
        # Calcular el nuevo costo promedio
        nuevo_costo_promedio = nuevo_costo_total / nueva_existencia
        # Asignar el nuevo costo promedio a la propiedad
        self.producto.precio_compra = nuevo_costo_promedio
        self.producto.save()  # Guarda el producto con el nuevo precio_compra
