from django.urls import path
from . import views


urlpatterns = [
    path('', views.contact, name='contact'),
    path('all-messages/', views.site_messages, name='site_messages'),
    path('message/<int:pk>/', views.view_message, name='view_message'),
    path('message/edit/<int:pk>/', views.edit_message, name='edit_message'),
    path('delete/<int:pk>/', views.delete_message, name='delete_message'),
]
