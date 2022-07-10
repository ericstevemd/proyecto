from django.urls import path

from devolucion import views



urlpatterns = [
    path('devolucion/', views.devolucion_list),
    path('devolucion/<int:pk>',views.devolucion_detail),
]
