from django.contrib import admin
from producto.models import *

from user.models import User
# Register your models here.

admin.site.register(proveedor)
admin.site.register(porducto)
admin.site.register(User)
admin.site.register(cliente)
admin.site.register(factura)

admin.site.register(tipoDocumento)
admin.site.register(ciudad)
admin.site.register(categoria)
admin.site.register(devolucion)
admin.site.register(tipo_articulo)



admin.site.register(formapago)
admin.site.register(detallefactura)