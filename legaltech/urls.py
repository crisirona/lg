from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('', views.Index, name='index'),
    path('nuevocaso/',login_required(views.nuevoCaso), name='nuevocaso'),
    path('listacasos/',login_required(views.listaCasos), name='listacasos'),
    path('listacasosaction/',login_required(views.listaCasosAction), name='listacasosaction'),
    path('detallenuevocaso/',login_required(views.detalleNuevoCaso), name='detallenuevocaso'),
    path('detallenuevademanda/',login_required(views.detalleNuevaDemanda), name='detallenuevademanda'),
    path('detalledemandado/',login_required(views.detalleDemandado),name='detalledemandado'),
    path('detalledemandante/',login_required(views.detalleDemandante),name='detalledemandante'),
    path('nuevademanda/',login_required(views.nuevaDemanda), name='nuevademanda'),
    path('login/', views.AdminLogin.as_view(), name="login"),
    path('logout/', login_required(views.AdminLogout.as_view()), name="logout"),
    path('register/',views.register,name='register'),
    path('eliminarconf/<int:id>/',login_required(views.eliminarconf),name='eliminarconf'),
    path('eliminar/<int:id>/',login_required(views.eliminar),name='eliminar'),
    path('modificar/<int:id>/',login_required(views.modificar), name='modificar'),
    path('modificarcaso/<int:id>/',login_required(views.modificarCaso), name='modificarcaso'),
    path('modificardemanda/<int:id>/',login_required(views.modificarDemanda), name='modificardemanda'),
    path('search/',login_required(views.search),name='search'),
]