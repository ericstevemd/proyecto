from django.urls import path

from tipoDocumento import views



urlpatterns = [
    path('tipodocumento/', views.doc_list),
    path('tipodocumento/<int:pk>',views.doc_detail),
]


