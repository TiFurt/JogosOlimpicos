from django import forms
from .models import Competicao, Atleta, Resultado


class CompeticaoForm(forms.ModelForm):
    class Meta:
        model = Competicao
        fields = ['nome', 'data', 'local']

class AtletaForm(forms.ModelForm):
    class Meta:
        model = Atleta
        fields = ['nome', 'idade', 'altura', 'peso']

class ResultadoForm(forms.ModelForm):
    class Meta:
        model = Resultado
        fields = ['atleta', 'modalidade', 'competicao', 'resultado']