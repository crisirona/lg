from django.urls import path
from . import views

urlpatterns = [
    path('', views.Index, name='index'),
    path('nuevocaso/',views.nuevoCaso, name='nuevocaso'),
    path('listacasos/',views.listaCasos, name='listacasos'),
    path('detallenuevocaso/',views.detalleNuevoCaso, name='detallenuevocaso'),
    path('detallenuevademanda/',views.detalleNuevaDemanda, name='detallenuevademanda'),
    path('detalledemandado/',views.detalleDemandado,name='detalledemandado'),
    path('detalledemandante/',views.detalleDemandante,name='detalledemandante'),
    path('nuevademanda/',views.nuevaDemanda, name='nuevademanda'),
    
]