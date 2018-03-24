from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User

from django.views.generic import CreateView, TemplateView

from .models import Perfil

from .forms import SignUpForm


class SignUpView(CreateView):
    model = Perfil
    #model = User
    
    template_name = 'perfiles/Registro.html'
    form_class = SignUpForm
    
    
    

    def form_valid(self, form):
        '''
        En este parte, si el formulario es valido guardamos lo que se obtiene de él y usamos authenticate para que el usuario incie sesión luego de haberse registrado y lo redirigimos al index
        '''
        form.save()
        usuario = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password1')
        usuario = authenticate(username=usuario, password=password)
        login(self.request, usuario)
        return redirect('/')

class BienvenidaView(TemplateView):
   template_name = 'perfiles/bienvenida.html'
   
from django.contrib.auth.views import LoginView

class SignInView(LoginView):
    template_name = 'perfiles/iniciar_sesion.html'

from django.contrib.auth.views import LoginView, LogoutView 

class SignOutView(LogoutView):
    pass

   