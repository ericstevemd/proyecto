from django.urls import path

from formaPago import views



urlpatterns = [
    path('formapago/', views.froma_list),
    path('formapago/<int:pk>',views.froma_detail),
]
