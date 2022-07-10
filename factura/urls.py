from django.urls import path

from factura import views



urlpatterns = [
    path('factura/', views.factura_list),
    path('factura/<int:pk>',views.factura_detail),
]
