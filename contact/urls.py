from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.contact, name='contact'),
    path('all-messages/', views.site_messages, name='site_messages'),
    path('message/', views.view_message, name='view_message'),    #view message    'message/<int:pk>/'
    path('delete/<int:pk>/', views.delete_message, name='delete_message'),
    
]