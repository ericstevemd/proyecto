from django.urls import path

from clientes import views



urlpatterns = [
    path('clientes/', views.cliente_l),
    path('clientes/<int:pk>',views.cliente_d),
]
