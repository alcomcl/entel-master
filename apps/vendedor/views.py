from django.contrib.auth import authenticate, login, get_user_model
from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.utils.http import is_safe_url
from django.views.generic import CreateView, FormView, ListView, DetailView, UpdateView, DeleteView
from django.urls import reverse, reverse_lazy
from apps.vendedor.models import User
from .forms import LoginForm, RegistroForm
#********************************************************************
from rest_framework.views import APIView
from apps.vendedor.serializers import UserSerializer
import json
#********************************************************************

# Habilitamos el uso de mensajes en Django
from django.contrib import messages 
 
# Habilitamos los mensajes para class-based views 
from django.contrib.messages.views import SuccessMessageMixin 


class UserAPI(APIView):
    serializer = UserSerializer

    def get(self, request, format=None):
        lista = User.objects.all()
        response = self.serializer(lista, many=True)

        return HttpResponse(json.dumps(response.data), content_type='application/json')



class RegisterView(SuccessMessageMixin, CreateView):
    model = User
    form_class = RegistroForm
    template_name = "vendedor/register.html"
    success_message = 'Vendedor registrado con exito'
    success_url = reverse_lazy('logout')


class VendedorList(ListView):
    model = User
    template_name = 'vendedor/listar_vendedor.html'
    context_object_name = 'usuarios'
    queryset = User.objects.all()


class VendedorDetail(DetailView):
    model = User
    context_object_name = 'usuario'
    template_name = 'vendedor/ver_vendedor.html'


class VendedorUpdate(SuccessMessageMixin, UpdateView):
    model = User
    template_name = 'vendedor/register.html'
    form_class = RegistroForm
    success_message = 'Vendedor Actualizado Correctamente!!!'
    success_url = reverse_lazy('vendedor:listar_vendedor')

class VendedorDelete(SuccessMessageMixin, DeleteView) :
    model = User
    fields = "__all__"
    
    def get_success_url(self): 
        success_message = 'Vendedor Eliminado Correctamente !!!' 
        messages.success (self.request, (success_message))       
        return reverse('vendedor:listar_vendedor')


