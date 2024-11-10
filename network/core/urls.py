from django.urls import path
from . import views

app_name = 'core'


urlpatterns = [
    path('register/', views.UserCreateView.as_view(), name='register'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('home/', views.HomeView.as_view(), name='home'),
]