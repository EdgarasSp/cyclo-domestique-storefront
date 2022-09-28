from django.urls import path
from . import views


urlpatterns = [
    path('', views.profile, name='profile'),
    path('orders/', views.profile_orders, name='profile_orders'),
    path('orders/all/', views.site_orders, name='site_orders'),
    path('order/edit/<order_number>/', views.edit_order, name='edit_order'),
    path('order_history/<order_number>',
         views.order_history, name='order_history'),
]
