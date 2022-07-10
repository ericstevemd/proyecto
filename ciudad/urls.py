from django.urls import path

from ciudad import views



urlpatterns = [
    path('ciudad/', views.ciudad_list),
    path('ciudad/<int:pk>',views.ciudad_detail),
]
