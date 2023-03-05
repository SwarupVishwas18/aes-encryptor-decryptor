from unicodedata import name
from django.urls import path
from . import views
import django.contrib.auth.views as views_aut

app_name = 'encryptdecrypt'

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views_aut.LoginView.as_view(template_name='encryptdecrypt/login.html'), name='login'),
    path('home/', views.home, name='home'),
    path('decryptor/', views.decryptor, name='dec'),
    path('encryptor/', views.encryptor, name='enc'),
    path('register/', views.register, name='register'),
    path('logout/', views.logout_view, name='logout'),
    path('clear/', views.clear, name='clear'),
]