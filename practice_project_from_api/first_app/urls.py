from django.contrib import admin
from django.urls import path,include
from .import views

urlpatterns = [
    path('',views.DjangoForm, name='DjangoForm'),
    path('password/',views.PasswordForm,name='PasswordForm'),
    
]
