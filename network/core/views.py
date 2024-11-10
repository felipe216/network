from django.shortcuts import render
from  django.http import HttpResponseRedirect, HttpResponse
from django.views.generic import TemplateView
from django.contrib.auth import authenticate

from . import forms
# Create your views here.


class UserCreateView(TemplateView):
    template_name = 'core/register.html'


    def post(self, request, *args, **kwargs):
        form = forms.UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse(render(request, 'core/home.html'))
        return HttpResponse(render(request, 'core/register.html'))
    

class LoginView(TemplateView):
    template_name = 'core/login.html'

    def post(self, request, *args, **kwargs):
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password) 
        if user is not None:
            return HttpResponseRedirect((render(request, 'core/home.html')))
        else:
            return HttpResponse(render(request, 'core/login.html'), {'error': 'Usuário ou senha inválidos'})

class HomeView(TemplateView):
    template_name = 'core/home.html'
