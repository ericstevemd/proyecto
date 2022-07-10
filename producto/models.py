
from pydoc import describe
from unittest.util import _MAX_LENGTH
from django.db import models
from user.models import User



class tipo_articulo(models.Model):
    id_tipoarticulo=models.IntegerField(db_column='id_tipo_articulos')
    descripcion_articulo=models.CharField(db_column='descripcion_articulo',max_length=50)

    def __str__(self):
        return self.tipo_articulo
    class Meta:
         db_table='tbl_tipo_articulo'


class devolucion(models.Model):
    id_devolucion=models.AutoField(db_column='id_devolucion',primary_key=True)
    id_detallefactura=models.IntegerField(db_column='id_detallefactura')
    id_detalle_articulo=models.IntegerField(db_column='id_detalle_articulo')
    motivo=models.DecimalField(null=True, db_column='Monto',max_digits=20, decimal_places=2)
    fecha_devolucion=models.DateField(db_column='fecha_devolucion')
    cantidad=models.IntegerField(db_column='cantidad')


    def __str__(self):
        return self.devolucion
    class Meta:
         db_table='tbl_devolucion'


class categoria(models.Model):
    id_categoria=models.IntegerField(db_column='id_categoria')
    nombre=models.CharField(db_column='nombre',max_length=50)
    detalle=models.CharField(db_column='detalle',max_length=60)

    def __str__(self):
        return self.categoria
    class Meta:
         db_table='tbl_categoria'



class proveedor(models.Model):
    id_proveedor =models.AutoField(primary_key=True,db_column='id_proveedor')
    nombre_de_proveedor=models.CharField(db_column='nombre_de_proveedr',max_length=50)
    telefono_provedor=models.CharField(db_column='telefono_provedor',max_length=50)
    direccion=models.CharField(db_column='direccion',max_length=50)
    email_proveedor=models.CharField(db_column='email_proveedor',max_length=60)
    def __str__(self):
        return self.proveedor
    class Meta:
         db_table='tbl_proveedor'

class detallefactura(models.Model):
    id_detalleFactura=models.AutoField(primary_key=True,db_column="id_detalle_factura")
    cod_factura=models.CharField(db_column='cod_factura',max_length=40)
    cod_articulos=models.CharField(db_column='cod_articulos',max_length=40)
    cantidad=models.IntegerField(db_column='cantidad')
    total=models.DecimalField(db_column='total',max_digits=20, decimal_places=2)
    def __str__(self):
        return self.detallefactura
    class Meta:
         db_table='tbl_detallefactura'


class formapago(models.Model):
    id_formapago=models.AutoField(primary_key=True,db_column="id_formapago")
    descripcion_fromapago=models.CharField(db_column="descripcion_fromapago",max_length=40)

    def __str__(self):
        return self.formapago
    class Meta:
         db_table='tbl_formapago'


class factura(models.Model):
    id_factura=models.AutoField(primary_key=True)
    Nnm_factura=models.CharField(db_column='Nnm_factura',max_length=50)
    cod_cliente=models.CharField(db_column='cod_cliente',max_length=50)
    nombre_empleado=models.CharField(db_column='nombre_empleado',max_length=50)
    fecha_factura=models.DateField(db_column="fecha_factura")
    subtotal=models.DecimalField(db_column="subtotal",max_digits=20, decimal_places=2)
    total_factura=models.DecimalField(db_column="total_factura",max_digits=20, decimal_places=2)
    iva12=models.DecimalField(db_column="iva12%",max_digits=20, decimal_places=2)
    iva0=models.DecimalField(db_column="iva0%",max_digits=20, decimal_places=2)
    id_forma_de_pago=models.ForeignKey(formapago,db_column="id_forma_de_pago",on_delete=models.CASCADE)
    id_detalleFactura=models.ForeignKey(detallefactura,db_column="id_detalleFactura",on_delete=models.CASCADE)
    def __str__(self):
        return self.factura
    class Meta:
        db_table='tbl_factura'





class porducto(models.Model):
    id_articlo=models.AutoField(primary_key=True, db_column='id_articulo')
    descripcion=models.CharField(db_column='descripcio',max_length=50)
    precio_venta=models.DecimalField(null=True,db_column='precio_venta',max_digits=20, decimal_places=2)
    precio_costo=models.DecimalField(null=True,db_column='precio_costo',max_digits=20, decimal_places=2)
    stock=models.IntegerField(db_column='stock')
    id_tipo_articulo=models.ForeignKey(tipo_articulo,db_column='cod_tipo_articulo', on_delete=models.CASCADE)
    id_proveedor=models.ForeignKey(proveedor,db_column='id_proveedor',on_delete=models.CASCADE)#ya esta 
    fecha_ingreso=models.DateField(db_column='fecha_ingreso')
    id_devolucion=models.ForeignKey(devolucion,db_column='id_devolucion',on_delete=models.CASCADE)
    id_categoria=models.ForeignKey(categoria ,db_column='id_categoria',on_delete=models.CASCADE)
    id_factura=models.ForeignKey(factura,db_column='id_factura',on_delete=models.CASCADE)


    def __str__(self):
        return self.porducto
    class Meta:
         db_table='tbl_porducto'


class cliente(models.Model):
    id_cliente=models.AutoField(primary_key=True,db_column="id_cliente")
    documento=models.CharField(db_column="documento",max_length=40)
    cod_tipo_documento=models.CharField(db_column="cod_tipo_documento",max_length=40)
    nombre=models.CharField(db_column="nombre",max_length=40)
    apellido=models.CharField(db_column="apellido",max_length=40)
    direccion=models.CharField(db_column="direccion",max_length=80)
    telefono=models.CharField(db_column="telefono",max_length=12)
    id_factura=models.ForeignKey(factura,on_delete=models.CASCADE,db_column="id_factura")
    id_ciudad=models.IntegerField(db_column="id_cuidad")
    id_user=models.ForeignKey(User,on_delete=models.CASCADE,db_column="id_user")

    def __str__(self):
        return self.cliente
    class Meta:
         db_table='tbl_cliente'

class ciudad(models.Model):
    id_codigo_cuidad=models.ForeignKey(cliente,on_delete=models.CASCADE,db_column="id_codigo_cuidad")
    id_proveedor=models.ForeignKey(proveedor,on_delete=models.CASCADE,db_column="id_porveedor")
    nombre_cuidad= models.CharField(db_column="nombre_cuidad",max_length=40)
    
    def __str__(self):
        return self.cliente
    class Meta:
         db_table='tbl_ciudad' 



class tipoDocumento(models.Model):
    id_tipo_documento=models.ForeignKey(cliente, on_delete=models.CASCADE,db_column="id_tipo_documento")
    Descripcion=models.CharField(db_column="Descripcion",max_length=80)
    def __str__(self):
        return self.tipoDocumento
    class Meta:
         db_table='tbl_tipoDocumento' 





