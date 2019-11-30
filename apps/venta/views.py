from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, DetailView

from apps.venta.models import Venta, Detalle_Venta
from apps.venta.forms import VentaForm, DetalleVentaForm
from django import forms
from . import models
import datetime
from django.utils.timezone import utc
#********************************************************************
from rest_framework.views import APIView
from apps.venta.serializers import VentaSerializer
import json
#********************************************************************
from django.http import HttpResponse


class VentaAPI(APIView):
    serializer = VentaSerializer

    def get(self, request, format=None):
        lista = Venta.objects.all()
        response = self.serializer(lista, many=True)

        return HttpResponse(json.dumps(response.data), content_type='application/json')

class VentaCreate(CreateView) :
    model = Venta
    form_class = VentaForm
    template_name = 'venta/venta_form.html'
    success_url = reverse_lazy('venta:listar_venta')

    def get_success_url(self):
        return reverse('venta:listar_venta')
    
    

class VentaList(ListView):
    model = Venta
    template_name = 'venta/listar_venta.html'
    fecha_actual = datetime.datetime.now()

class DetalleDetail(DetailView) :
    model = Detalle_Venta
    context_object_name = 'venta'
    template_name = 'venta/detalle/detalle_venta.html'

    def get_context_data(self, **kwargs):
        context = super(DetalleDetail, self).get_context_data(**kwargs)
        context['productos'] = Detalle_Venta.objects.all()
        return context
