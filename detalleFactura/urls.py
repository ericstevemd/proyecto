from django.urls import path

from detalleFactura import views



urlpatterns = [
    path('datallefactura/', views.detalle_list),
    path('datallefactura/<int:pk>',views.detalle_detail),
]
