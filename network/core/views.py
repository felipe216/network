from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.views.generic import TemplateView
from django.contrib.auth import authenticate, login

from . import forms
# Create your views here.


class UserCreateView(TemplateView):
    template_name = 'core/register.html'


    def post(self, request, *args, **kwargs):
        form = forms.UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse(render(request, 'core/login.html'))
        return render(request, 'core/register.html', {'form': form})
    

class LoginView(TemplateView):
    template_name = 'core/login.html'

    def post(self, request, *args, **kwargs):
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is None:
            user = authenticate(request, email=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse('core:home'))
        else:
            return render(request, 'core/login.html')

class HomeView(TemplateView):
    template_name = 'core/home.html'

    def get(self, request, *args, **kwargs):
        print(request.user)
        return super().get(request, *args, **kwargs)
