
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
   
   path('admin/', admin.site.urls),
   path('api/v2/',include('user.urls')),
   path('api/v2/',include('rol.urls')),
   path('api/v2/',include('Proveedor.urls')),

   path('api/v2/',include('producto.urls')),
   path('api/v2/',include('categoria.urls')),
   path('api/v2/',include('clientes.urls')),
   path('api/v2/',include('detalleFactura.urls')),
 
   path('api/v2/',include('tipoArticulo.urls')),
   path('api/v2/',include('tipoDocumento.urls')),
   path('api/v2/',include('ciudad.urls')),
   path('api/v2/',include('formaPago.urls')),
   path('api/v2/',include('devolucion.urls')),
   path('api/v2/',include('factura.urls')),


  
  
]