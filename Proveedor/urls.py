from django.urls import path

from Proveedor import views



urlpatterns = [
    path('proveedor/', views.proveedor_list),
    path('proveedor/<int:pk>',views.proveerdo_detail),
]
