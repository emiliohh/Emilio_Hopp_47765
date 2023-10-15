from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class colegio(models.Model):
    nombre= models.CharField(max_length=30)
    direccion= models.CharField(max_length=30)
    email = models.EmailField()
    dependencia= models.CharField(max_length=30)
    
class actividad_ep(models.Model):
    nombre = models.CharField(max_length=30)
    periodicidad = models.CharField(max_length=30)
    duracion =  models.IntegerField()
    
class infra(models.Model):
    nombre = models.CharField(max_length=30)
    descripcion = models.CharField(max_length=30)
    tamaño =  models.IntegerField()
    tipo = models.CharField(max_length=30)

class beca(models.Model):
    nombre = models.CharField(max_length=30)
    descripcion = models.CharField(max_length=30)

class Avatar(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to="avatares", null=True, blank=True)