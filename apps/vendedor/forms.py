from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.contrib.auth import authenticate

from .models import User


User = get_user_model()

class UserAdminChangeForm(forms.ModelForm): # Formulario para actualizar usuarios. Incluye todos los campos de usuario
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = User
        fields = (('nombre','apellido_paterno','apellido_materno', 'email','fecha_nacimiento','password','active','admin'))

    def clean_password(self):
        return self.initial["password"]



class LoginForm(forms.Form):
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'class':'form-control',
                        'placeholder':'duoc@entel.cl'})) 
    password = forms.CharField(label='Contraseña', widget=forms.PasswordInput(attrs={'class':'form-control',
                        'placeholder':'Ingrese su Contraseña'}))
    

    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email = email).exists():
            pass
        else:
            raise forms.ValidationError("Este email no pertenece a ningun usuario")
        return email
    
   
    


class RegistroForm(forms.ModelForm): # Formulario para crear usuarios nuevos. Incluye campos obligatorios y confirmacion de contraseña
    nombre            = forms.CharField(label='Nombre', widget=forms.TextInput(attrs={'class':'form-control',
                        'placeholder':'Ingrese nombre del vendedor'}))
    apellido_paterno  = forms.CharField(label='Apellido Paterno', widget=forms.TextInput(attrs={'class':'form-control',
                        'placeholder':'Ingrese apellido paterno'}) )
    apellido_materno  = forms.CharField(label='Apellido Materno', widget=forms.TextInput(attrs={'class':'form-control',
                        'placeholder':'Ingrese apellidos materno'}) )
    email             = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'class':'form-control',
                        'placeholder':'Ingrese un correo electronico valido'})) 
    fecha_nacimiento  = forms.DateField(label='Fecha Nacimiento', widget=forms.DateInput(attrs={'class':'form-control',
                        'placeholder':'Siga este formato YYYY-MM-DD'}) )
    password1         = forms.CharField(label='Contraseña', widget=forms.PasswordInput(attrs={'class':'form-control',
                        'placeholder':'Ingrese una contraseña minimo 6 caracteres'}))
    password2         = forms.CharField(label='Confirmar Contraseña', widget=forms.PasswordInput(attrs={'class':'form-control',
                        'placeholder':'Repita la Contraseña'}) )

    class Meta:
        model = User
        fields = ('nombre',
                  'apellido_paterno',
                  'apellido_materno',
                  'email',
                  'fecha_nacimiento',
                  )

    def clean_password2(self):
        
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("No hubo coincidencias con la Contraseña")
        return password2

    def save(self, commit=True):
        user = super(RegistroForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        #user.active = False # envia confirmacion de email Este campo deja inactivo al usuario una vez creado
        if commit:
            user.save()
        return user

