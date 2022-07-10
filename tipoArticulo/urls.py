from django.urls import path

from tipoArticulo import views



urlpatterns = [
    path('tipoarticulo/', views.art_list),
    path('tipoarticulo/<int:pk>',views.art_detail),
]


