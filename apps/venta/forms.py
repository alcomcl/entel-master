from apps.venta.models import Venta, Detalle_Venta
from django import forms
"""
class VentaForm(forms.ModelForm):
    
    class Meta:
        model = Venta

        fields = [          
            'vendedor',
            'producto',
            'total_venta',
        ]
        label = {
            'vendedor': 'Vendedor Actual',
            'producto': 'Seleccione Producto',
            'total_venta': 'Indique Precio Venta',
        }
        widget = {
            'vendedor': forms.Select(attrs={'class':'form-control'}),
            'producto': forms.SelectMultiple().allow_multiple_selected,
            'total_venta': forms.TextInput(attrs={'class':'form-control',
                        'placeholder':'Ingrese un precio para esta venta'}),
        }
"""
class VentaForm(forms.ModelForm):
    class Meta:
        model = Venta
        fields = ('vendedor', 'producto', 'total_venta')
        widgets = {
            'producto': forms.SelectMultiple(attrs={"class":"pene"}),          
        }


class DetalleVentaForm(forms.ModelForm) :

    class Meta:
        model = Detalle_Venta
        fields = [
            'cant_producto'
        ]
        labels = {
            'cant_producto': 'Cantidad',
        }
        widget = {
            'cant_producto':forms.TextInput(attrs={'class': 'form-control'}),
        }