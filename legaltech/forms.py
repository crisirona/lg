from django import forms

from .models import Caso, Demanda, Demandado,Demandante

class CasoForm(forms.ModelForm):

    class Meta:
        model = Caso
        fields = ('id_caso','author' )

class DemandaForm(forms.ModelForm):

    class Meta:
        model = Demanda
        fields = ('caso','id_demanda','author','fecha','hora','tipodemanda','detalle' )

class DemandadoForm(forms.ModelForm):

    class Meta:
        model = Demandado
        fields = ('rut','dv','nombre','apellido','telefono','demanda' )

class DemandanteForm(forms.ModelForm):

    class Meta:
        model = Demandante
        fields = ('rut','dv','nombre','apellido','telefono','demanda' )

      