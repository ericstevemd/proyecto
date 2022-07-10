from django.urls import path

from categoria import views



urlpatterns = [
    path('categoria/', views.categoria_l),
    path('categoria/<int:pk>',views.categoria_d),
]
