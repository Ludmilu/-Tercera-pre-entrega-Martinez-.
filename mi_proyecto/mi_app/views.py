from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .models import Producto
from .forms import ProductoForm

def producto_nuevo(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = ProductoForm()
    return render(request, 'mi_app/producto_nuevo.html', {'form': form})

