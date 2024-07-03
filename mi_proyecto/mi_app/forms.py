# En forms.py de mi_app

from django import forms
from .models import Categoria, Producto

class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ['nombre']

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre', 'categoria', 'precio']

class BusquedaForm(forms.Form):
    termino_busqueda = forms.CharField(label='Buscar')
