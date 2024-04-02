from django import forms
from django.core.exceptions import ValidationError
from .models import Compra
from Apps.inventario.models import Producto

class CompraForm(forms.ModelForm):
    producto = forms.ModelChoiceField(queryset=Producto.objects.all())
    observaciones = forms.CharField(required=False, widget=forms.Textarea(attrs={'rows': 3}))

    class Meta:
        model = Compra
        fields = ['producto', 'costo_compra', 'cantidad', 'observaciones']

    def clean_costo_compra(self):
        costo_compra = self.cleaned_data['costo_compra']
        if costo_compra < 0:
            raise ValidationError("El costo de compra no puede ser un número negativo.")
        return costo_compra

    def clean_cantidad(self):
        cantidad = self.cleaned_data['cantidad']
        if cantidad < 0:
            raise ValidationError("La cantidad no puede ser un número negativo.")
        return cantidad
