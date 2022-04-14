from urllib import request
from django.conf import settings
from django.db import models
from django.utils import timezone




class Caso(models.Model):
    id_caso = models.IntegerField()
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __Str__(self):
        return self.id_caso

class Demanda(models.Model):
    id_demanda = models.IntegerField()
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    fecha = models.DateField(default=timezone.now)
    hora = models.TimeField()
    tipodemanda = models.CharField(max_length=30)
    detalle = models.TextField()
    caso = models.ForeignKey(Caso,on_delete=models.CASCADE)

    def __Str__(self):
        return self.id_demanda

class Demandado(models.Model):
    rut = models.IntegerField()
    dv = models.IntegerField()
    nombre = models.CharField(max_length=25)
    apellido = models.CharField(max_length=25)
    telefono = models.IntegerField()

    demanda = models.ForeignKey(Demanda, on_delete=models.CASCADE)

    def __Str__(self):
        return self.rut

class Demandante(models.Model):
    rut = models.IntegerField()
    dv = models.IntegerField()
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    telefono = models.IntegerField()

    demanda = models.ForeignKey(Demanda, on_delete=models.CASCADE)

    def __Str__(self):
        return self.rut

