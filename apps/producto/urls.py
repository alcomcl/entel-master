from django.urls import path
from .views import Home, ProductoList, ProductoCreate, ProductoUpdate, ProductoDetail, ProductoDelete, ProductoUpdate
from .views import TipoProductoList, TipoProductoCreate, TipoProductoUpdate, TipoProductoDelete
from django.contrib.auth.decorators import login_required
from apps.producto.views import ProductoAPI


urlpatterns = [

    # Urls Modelo Producto
    path('home/',Home.as_view(), name='home'),
    path('producto/listar_producto/', login_required( ProductoList.as_view() ), name='listar_producto'),
    path('producto/crear_producto/', login_required( ProductoCreate.as_view() ), name='crear_producto'),
    path('producto/editar_producto/<int:pk>', login_required( ProductoUpdate.as_view() ), name='editar_producto'),
    path('producto/ver_producto/<int:pk>', login_required( ProductoDetail.as_view() ), name='ver_producto'),
    path('producto/eliminar_producto/<int:pk>', login_required( ProductoDelete.as_view() ), name='eliminar_producto'),
    
    # Urls Modelo Tipos de Productos
    path('categorias/', login_required( TipoProductoList.as_view() ), name='categorias' ),
    path('categorias/crear_categoria', login_required( TipoProductoCreate.as_view() ), name='crear_categoria' ),
    path('categorias/editar_categoria/<int:pk>', login_required( TipoProductoUpdate.as_view() ), name='editar_categoria'),
    path('categorias/eliminar_categoria/<int:pk>', login_required( TipoProductoDelete.as_view() ), name='eliminar_categoria' ),

    # API Productos
    path('productos/productosAPI', ProductoAPI.as_view() , name='api-productos'),

]