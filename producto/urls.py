from django.urls import path

from producto import views



urlpatterns = [
    path('producto/', views.prod_list),
    path('producto/<int:pk>',views.prod_detail),
]
