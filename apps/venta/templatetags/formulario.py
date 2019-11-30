import re
from django import template
from django.urls import reverse, NoReverseMatch, reverse_lazy
from datetime import date
from apps.venta import models as modelos
register = template.Library()

@register.simple_tag()
def fecha():
    return date.today()
  

@register.simple_tag()
def productos():
    return modelos.Producto.objects.all()



    