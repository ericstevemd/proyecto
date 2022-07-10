
from django.db import models

class User(models.Model):
    idUser=models.AutoField(primary_key=True,db_column='id_user')
    nombre=models.CharField(max_length=50, db_column='nombre')
    apellido=models.CharField(max_length=50 ,db_column='apellido')
    direccion=models.CharField(max_length=80 , db_column='direccion')
    email=models.CharField(max_length=60,db_column='email')
    user=models.CharField(max_length=30,db_column='user')
    clave=models.CharField(max_length=30,db_column='clave')
    fechaingreso=models.DateField(db_column='fecha_inicio')
    fechaultima=models.DateField(db_column='fecha_ultiomos_inicio')
    idrol=models.IntegerField(db_column='id_rol')

    def __str__(self):
        return self.User

    class Meta:
        db_table='tbl_user'

 
