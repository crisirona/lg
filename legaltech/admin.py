from django.contrib import admin
from .models import Caso,Demanda ,Tipodemanda,Comuna

admin.site.register(Caso)
admin.site.register(Demanda)
admin.site.register(Comuna)
admin.site.register(Tipodemanda)
