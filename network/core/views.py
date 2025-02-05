import json
from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.db import IntegrityError
from django.views.generic import TemplateView
from django.contrib.auth import authenticate, login

from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Post, Like

from .serializers import PostSerializer

from . import forms
# Create your views here.


class UserCreateView(TemplateView):
    template_name = 'core/register.html'


    def post(self, request, *args, **kwargs):
        form = forms.UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('core:perfil_form'))
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
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse('core:home'))
        else:
            return render(request, 'core/login.html')

class HomeView(TemplateView):
    template_name = 'core/home.html'

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        posts = Post.objects.all()

        serializer = PostSerializer(list(posts), many=True, context={'request': self.request})
        ctx['posts'] = json.dumps(serializer.data)
        return ctx

class PerfilCreateView(TemplateView):
    template_name = 'core/perfil_form.html'

    def post(self, request, *args, **kwargs):
        form = forms.PerfilForm(request.POST)
        if form.is_valid():
            form.instance.user = request.user
            try:
                form.save()
            except IntegrityError:
                return render(request, 'core/perfil_form.html', {'form': form, 'error': 'Perfil já cadastrado'})
            return HttpResponseRedirect(reverse('core:home'))
        return render(request, 'core/perfil_form.html', {'form': form})
    
    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['form'] = forms.PerfilForm()
        return ctx
    

class NewPostView(APIView):

    def post(self, request, *args, **kwargs):
        text = request.data["text"]
        user = request.user
        post = Post(text=text, author=user)
        try:
            post.save()
            post =  PostSerializer(post).data
            return Response(post, status=200)
        except:
            return HttpResponse(status=400)
        

class LikeView(APIView):

    def post(self, request, *args, **kwargs):
        post_id = request.data["post"]
        comment_id = request.data.get("comment", None)
        user = request.user
        post = Post.objects.get(id=post_id)
        like = post.likes.filter(user=user, comment=comment_id, post=post)
        if like.exists():
            like.delete()
            return Response({"liked": False}, status=200)
        else:
            like = Like(post=post, user=user, comment=comment_id)
            like.save()
            return Response({"liked": True}, status=200)