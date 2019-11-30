
from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .forms import UserAdminChangeForm, RegistroForm
from .models import User




class UserAdmin(BaseUserAdmin):
    form = UserAdminChangeForm # Vista Actualizar
    add_form = RegistroForm # Vista Crear

    
    list_display = ('email', 'admin')
    list_filter = ('admin',)
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Datos Personales', {'fields': ('nombre','apellido_paterno','apellido_materno','fecha_nacimiento')}),
        ('Permisos', {'fields': ('admin','staff','active')}),
    )
    
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2')}
        ),
    )
    search_fields = ('email',)
    ordering = ('email',)
    filter_horizontal = ()


admin.site.register(User, UserAdmin)




# Eliminamos el modelo Grupo del administrador de Django
admin.site.unregister(Group)
