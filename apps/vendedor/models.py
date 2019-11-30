from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser, BaseUserManager
) 

class UserManager(BaseUserManager):
    def create_user(self, email,password=None, is_active=True, is_staff=False, is_admin=False):
        if not email:
            raise ValueError("Debe ingresar un Correo Electronico")
        if not password:
            raise ValueError('Debe ingresar una contraseña')
        user = self.model( email = self.normalize_email(email), )
        user.set_password(password) # Usuario cambia la contraseña
        user.staff = is_staff
        user.admin = is_admin
        user.active = is_active
        user.save(using=self._db)
        return user


    def create_staffuser(self, email, password=None):
        user = self.create_user(email, password=password)
        user.staff = True
        user.save(using=self._db)
        return user
    

    def create_superuser(self, email, password=None):
        user = self.create_user(email, password=password)
        user.staff = True
        user.admin = True
        user.save(using=self._db)
        return user



class User(AbstractBaseUser):
    nombre              = models.CharField(max_length=200, null=False, blank=False)
    apellido_paterno    = models.CharField(max_length=200, null=False, blank=False)
    apellido_materno    = models.CharField(max_length=200, null=False, blank=False)
    email               = models.EmailField(max_length=255, unique=True)
    fecha_nacimiento    = models.DateField(null =True, blank=True)
    active              = models.BooleanField(default=True) # podrá logearse
    staff               = models.BooleanField(default=False) # usuario comun, no admnistrador
    admin               = models.BooleanField(default=False) # administrador(superuser)

    USERNAME_FIELD = 'email' #nombre de usuario para el sistema
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return self.nombre + ' ' + self.apellido_paterno + ' ' + self.apellido_materno
    
    def get_full_name(self):
        return self.email
    
    def get_short_name(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True
    
    def has_module_perms(self, app_label):
        return True
    
    @property
    def is_staff(self):
        return self.staff

    @property
    def is_admin(self):
        return self.adimin

    @property
    def is_active(self):
        return self.active
