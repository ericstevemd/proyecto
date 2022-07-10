from django.urls import path

from rol import views



urlpatterns = [
    path('rol/', views.rol_list),
    path('rol/<int:pk>',views.rol_detail),
]


