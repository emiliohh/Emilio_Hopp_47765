from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from colegios.models import Avatar


class UsuarioRegistro(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repetir la contraseña', widget=forms.PasswordInput) 
   
    #imagen_avatar = forms.ImageField(required=False)

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2'] 
        #Saca los mensajes de ayuda
        #help_texts = {k:"" for k in fields}
 
class FormularioEditar(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repetir la contraseña', widget=forms.PasswordInput) 
   
    #imagen_avatar = forms.ImageField(required=False)

    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name', 'password1', 'password2'] 
        #Saca los mensajes de ayuda
        #help_texts = {k:"" for k in fields}
        
class AvatarFormulario(forms.ModelForm):
    class Meta:
        model = Avatar
        fields = ["imagen"]