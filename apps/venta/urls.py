from django.urls import path
from django.contrib.auth.decorators import login_required
from .views import VentaCreate, VentaList, DetalleDetail
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required
from apps.venta.views import VentaAPI


urlpatterns = [
     path('venta/crear_venta/', login_required( VentaCreate.as_view() ), name="crear_venta"),
     path('venta/listar_venta/', login_required( VentaList.as_view() ), name="listar_venta"),
     path('venta/detalle_venta/<int:pk>', login_required( DetalleDetail.as_view() ), name="detalle_venta"),

     # API Ventas

    path('venta/ventasApi', VentaAPI.as_view(), name='api-usuarios'),


]
