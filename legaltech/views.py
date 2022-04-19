from django.shortcuts import redirect, render
from .forms import CasoForm , DemandaForm,NewUserForm
from .models import Caso, Demanda
from django.contrib.auth.views import LoginView, LogoutView
from django.db.models import Q

def Index(request):
    
    return render(request, 'legaltech/index.html')

def nuevoCaso(request):
    return render(request,'legaltech/nuevocaso.html')

def nuevaDemanda(request):
    return render(request,'legaltech/nuevademanda.html')

def detalleNuevoCaso(request):
    
    if request.method == 'POST':
        form = CasoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('detallenuevademanda')
    else:
        form = CasoForm()

    contexto ={
        'form': form
    }
    return render(request,'legaltech/detallenuevocaso.html',contexto)

def detalleNuevaDemanda(request):
    case = Caso.objects.last()
    if request.method == 'POST':
        form = DemandaForm(request.POST)
        if form.is_valid():
            deman=form.save(commit=False)
            deman.id_caso=case
            deman.author = request.user
            deman.save()
            return redirect('listacasos')
    else:
        form = DemandaForm()

    contexto ={
        'form': form
    }
    return render(request,'legaltech/detallenuevademanda.html',contexto)

def detalleDemandado(request):
    
    # if request.method == 'POST':
    #     form = DemandadoForm(request.POST)
    #     if form.is_valid():
    #         form.save()
    #         return redirect('detalledemandante')
    # else:
    #     form = DemandadoForm()

    contexto ={
        # 'form': form
    }
    return render(request,'legaltech/detalledemandado.html',contexto)

def detalleDemandante(request):
    
    # if request.method == 'POST':
    #     form = DemandanteForm(request.POST)
    #     if form.is_valid():
    #         form.save()
    #         return redirect('listacasos')
    # else:
    #     form = DemandanteForm()

    contexto ={
        # 'form': form
    }
    return render(request,'legaltech/detalledemandante.html',contexto)

def listaCasos(request):
    casos = Caso.objects.all()
    contexto = {
        'casos': casos
    }
    return render(request,'legaltech/listacasos.html',contexto)

def listaCasosAction(request):
    casos = Caso.objects.all()
    contexto = {
        'casos': casos
    }
    return render(request,'legaltech/listacasosaction.html',contexto)

class AdminLogin(LoginView):
    template_name = 'legaltech/accounts/login.html'


class AdminLogout(LogoutView):
    pass

def register(request):
    if request.method == 'POST':  
        form = NewUserForm(request.POST)  
        if form.is_valid():  
            form.save()  
            return redirect('index')
    else:  
        form = NewUserForm()  
    context = {  
        'form':form  
    }  
    return render(request,'legaltech/accounts/register.html',context)

def eliminarconf(request,id):
    caso = Caso.objects.get(id_caso=id)
    demanda=Demanda.objects.get(id_caso=caso)
    contexto={
        'caso':caso,
        'demanda':demanda,
    }
    return render(request,'legaltech/eliminarconf.html',contexto)

def eliminar(request,id):
    caso = Caso.objects.get(id_caso=id)
    demanda=Demanda.objects.get(id_caso=caso)
    caso.delete()
    demanda.delete()
    return redirect('listacasos')

def modificar(request,id):
    caso = Caso.objects.get(id_caso=id)
    demanda=Demanda.objects.get(id_caso=caso)
    contexto={
        'caso':caso,
        'demanda':demanda,
    }
    return render(request,'legaltech/modificar.html',contexto)

def modificarDemanda(request,id):
    caso = Caso.objects.get(id_caso=id)
    demanda = Demanda.objects.get(id_caso=caso)
    formulario = DemandaForm(request.POST or None, request.FILES or None, instance=demanda)
    contexto={
        'demanda':demanda,
        'form':formulario
    }
    return render(request,'legaltech/modificardemanda.html',contexto)


def modificarCaso(request,id):
    caso = Caso.objects.get(id_caso=id)
    formulario = CasoForm(request.POST or None, request.FILES or None, instance=caso)
    contexto={
        'caso':caso,
        'formulario':formulario
    }
    return render(request,'legaltech/modificarcaso.html',contexto)

def search(request):
    busqueda = request.GET.get("buscar")
    caso = Caso.objects.all()
    if busqueda:
        caso = Caso.objects.filter(
            Q(id_caso__icontains= busqueda)
        ).distinct()
        
    
    contexto={
        'caso':caso,
        
    }
    return render(request,'legaltech/search.html',contexto)