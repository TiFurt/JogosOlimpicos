from django.urls import path
from .views import addAtleta, deleteCompeticoes, deleteAtletas, addResultado, index, ranking, deleteResultados

urlpatterns = [
    path('', index, name='index'),
    path('addAtleta/', addAtleta, name='addAtleta'),
    path('deleteCompetições/', deleteCompeticoes, name='deleteCompeticoes'),
    path('deleteAtletas/', deleteAtletas, name='deleteAtletas'),
    path('addResultado/', addResultado, name='addResultado'),
    path('resultado/', addResultado, name='addResultado'),
    path('ranking/', ranking, name='ranking'),
    path('deleteResultados/', deleteResultados, name='deleteResultados')
]
