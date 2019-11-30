from django import forms
from apps.producto.models import Producto, tipoProducto

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = [
            'nombre',
            'precio',
            'tipoProducto',
            #'imagen',
        ]
        label = {
            'nombre' : 'Nombre',
            'precio' : 'Precio',
            'tipoProducto': 'Categoria',
            #'imagen': 'Imagen',
        }
        widget = {
            'nombre': forms.Textarea(attrs={'class':'form-control'}),
            'precio': forms.TextInput(attrs={'class':'form-control'}),
            'tipoProducto': forms.Select(attrs={'class':'form-control'}),
            #'imagen' : forms.ImageField(),
        }

class TipoProductoForm(forms.ModelForm):

    class Meta:
        model = tipoProducto

        fields = [
            'nombre',
        ]
        label = {
            'nombre':'Nombre Categoria',
        }
        widgets = {
            'nombre': forms.TextInput(attrs={'class':'form-control', 
            'placeholder': 'Ingrese el nombre de una categoria valida'}),
        }