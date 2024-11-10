from django.shortcuts import render
from django.views.generic import TemplateView

from . import forms
# Create your views here.


class UserCreateView(TemplateView):
    template_name = 'core/register.html'

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['form'] = forms.UserForm()
        return ctx
