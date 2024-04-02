from django import forms
from .models import Cliente

class ClienteienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nombre', 'saldo']
