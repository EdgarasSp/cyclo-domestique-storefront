from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.contact, name='contact'),
    path('contact/site/', views.site_messages, name='site_messages'),
]