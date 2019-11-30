from django.urls import path
from django.contrib.auth.decorators import login_required
from .views import RegisterView, VendedorList, VendedorDetail, VendedorDelete, VendedorUpdate
from django.contrib.auth import views as auth_views
from apps.vendedor.views import UserAPI
#from .views import LoginView


urlpatterns = [
    path('vendedor/listar_vendedor/',login_required( VendedorList.as_view() ), name='listar_vendedor'),
    #path('login/', LoginView.as_view() , name='login_vendedor'),
    path('vendedor/crear_vendedor/', RegisterView.as_view(), name='crear_vendedor'),
    path('vendedor/ver_vendedor/<int:pk>', login_required( VendedorDetail.as_view() ), name='ver_vendedor' ),
    path('vendedor/editar_vendedor/<int:pk>', login_required( VendedorUpdate.as_view() ), name='editar_vendedor'  ),
    path('vendedor/eliminar_vendedor/<int:pk>', login_required( VendedorDelete.as_view() ), name='eliminar_vendedor' ),
    
    
    # API Uusarios

    path('usuario/usuariosAPI', UserAPI.as_view(), name='api-usuarios'),

]