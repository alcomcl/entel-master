from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.db import models
from django.views.generic import TemplateView, ListView, UpdateView, CreateView, DetailView, DeleteView
from django.http import HttpResponse
from apps.producto.models import Producto, tipoProducto
from apps.producto.forms import ProductoForm, TipoProductoForm
#********************************************************************
from rest_framework.views import APIView
from apps.producto.serializers import ProductoSerializer
import json
#********************************************************************

# Habilitamos el uso de mensajes en Django
from django.contrib import messages 
 
# Habilitamos los mensajes para class-based views 
from django.contrib.messages.views import SuccessMessageMixin 


class ProductoAPI(APIView):
    serializer = ProductoSerializer

    def get(self, request, format=None):
        lista = Producto.objects.all()
        response = self.serializer(lista, many=True)

        return HttpResponse(json.dumps(response.data), content_type='application/json')


class Home(TemplateView):
    template_name = 'base/index.html'


class ProductoList(ListView):
    model = Producto
    template_name = 'producto/listar_producto.html'
    context_object_name = 'productos'
    queryset = Producto.objects.all()

class ProductoCreate(SuccessMessageMixin, CreateView):
    model = Producto
    #form_class = ProductoForm
    template_name = 'producto/producto_form.html'
    fields = "__all__" 
    success_message = 'Producto Registrado Correctamente!!!'
    success_url = reverse_lazy('producto:listar_producto')

class ProductoUpdate(UpdateView):
    model = Producto
    form_class = ProductoForm
    template_name = 'producto/producto_form.html'
    success_url = reverse_lazy('producto:listar_producto')

class ProductoDetail(DetailView):
    model = Producto
    template_name = 'producto/ver_producto.html'

class ProductoDelete(SuccessMessageMixin, DeleteView) :
    model = Producto
    form = Producto
    fields = "__all__"
    
    def get_success_url(self): 
        success_message = 'Producto Eliminado Correctamente !!!' 
        messages.success (self.request, (success_message))       
        return reverse('producto:listar_producto') 





# VISTAS MODELO TIPO PRODUCTO

class TipoProductoList(ListView):
    model = tipoProducto
    template_name = 'producto/tipo/listar_tipo.html'
    context_object_name = 'tipoProductos'
    queryset = tipoProducto.objects.all()

class TipoProductoCreate(SuccessMessageMixin, CreateView):
    model = tipoProducto
    form_class = TipoProductoForm
    template_name = 'producto/tipo/tipo_form.html'
    success_message = 'Categoria registrada con Exito!!!'
    success_url = reverse_lazy('producto:categorias')


class TipoProductoDelete(SuccessMessageMixin, DeleteView) :
    model = tipoProducto
    form = tipoProducto
    fields = "__all__"
    
    def get_success_url(self): 
        success_message = 'Categoria Eliminada Correctamente !!!' 
        messages.success (self.request, (success_message))       
        return reverse('producto:categorias') 


class TipoProductoUpdate(SuccessMessageMixin, UpdateView):
    model = tipoProducto
    form_class = TipoProductoForm
    template_name = 'producto/tipo/tipo_form.html'
    success_message = 'Categoria actualizada con Exito!!!'
    success_url = reverse_lazy('producto:categorias')

