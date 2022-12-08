from django.db import models
import datetime

class familiar(models.Model):
    id = models.AutoField(primary_key=True, unique=True) 
    nombre = models.CharField(max_length=100, null=False)
    apellido = models.CharField(max_length=100, null=False)
    edad = models.IntegerField(null=False)  
    email = models.CharField(max_length=100, null=False)
    tel_movil = models.IntegerField(null=False)
    fecha = models.DateField(null=False)
    
    @classmethod
    def create(self, nombre:str, apellido:str, edad: int, email:str, tel_movil:int, fecha:datetime.date): 
        return self(nombre=nombre, apellido=apellido, edad=edad, email=email, tel_movil=tel_movil, fecha=fecha)