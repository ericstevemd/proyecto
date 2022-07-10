from django.db import models
from user.models import User




class rol(models.Model):
    idrol=models.ForeignKey(User,blank=True,db_column='id_rol',on_delete=models.CASCADE)
    rol=models.CharField(max_length=50,db_column='rol')
    tipo_rol=models.IntegerField(db_column='tipo_rol')
    
    def __str__(self):
        return self.rol
    class Meta:
         db_table='tbl_rol'