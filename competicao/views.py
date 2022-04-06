from django.shortcuts import render, redirect
from .models import Competicao, Atleta, Resultado, Modalidade
from .forms import CompeticaoForm, AtletaForm, ResultadoForm


# Create your views here.
def index(request):
    formCompeticao = CompeticaoForm(request.POST or None)
    competicoes = Competicao.objects.all()
    if formCompeticao.is_valid():
        formCompeticao.save()
        return redirect('addAtleta')

    return render(request, 'index.html', {'formCompeticao': formCompeticao, 'competicoes': competicoes})


def addAtleta(request):
    formAtleta = AtletaForm(request.POST or None)
    atletas = Atleta.objects.all()
    if formAtleta.is_valid():
        formAtleta.save()

    return render(request, 'atleta.html', {'formAtleta': formAtleta, 'atletas': atletas})


def deleteCompeticoes(request):
    competicao = Competicao.objects.all()
    competicao.delete()
    return redirect('index')


def deleteAtletas(request):
    atleta = Atleta.objects.all()
    atleta.delete()
    return redirect('addAtleta')


def addResultado(request):
    formResultado = ResultadoForm(request.POST or None)
    atletas = Atleta.objects.all()
    modalidades = Modalidade.objects.all()
    resultados = Resultado.objects.all()
    if formResultado.is_valid():
        formResultado.save()
    return render(request, 'resultado.html',
                  {'formResultado': formResultado, 'atletas': atletas, 'modalidades': modalidades,
                   'resultados': resultados})


def deleteResultados(request):
    resultado = Resultado.objects.all()
    resultado.delete()
    return redirect('addResultado')


def ranking(request):
    resultados100m = Resultado.objects.filter(modalidade__nome='100m Rasos')
    resultadosLancamento = Resultado.objects.filter(modalidade__nome='Lançamento de Dardos')
    dictresultados100m = {}
    dictresultadosLancamento = {}
    for resultado in resultados100m:
        dictresultados100m[resultado.atleta] = resultado.resultado
    for resultado in resultadosLancamento:
        dictresultadosLancamento[resultado.atleta] = resultado.resultado
    sorted100m = sorted(dictresultados100m.items(), key=lambda x: x[1])
    sortedLancamento = sorted(dictresultadosLancamento.items(), key=lambda x: x[1], reverse=True)
    return render(request, 'ranking.html', {'sorted100m': sorted100m, 'sortedLancamento': sortedLancamento,
                                            'dictresultados100m': dictresultados100m,
                                            'dictresultadosLancamento': dictresultadosLancamento})
