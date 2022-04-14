from django.contrib import admin
from .models import Caso,Demanda,Demandado,Demandante

admin.site.register(Caso)
admin.site.register(Demanda)
admin.site.register(Demandado)
admin.site.register(Demandante)