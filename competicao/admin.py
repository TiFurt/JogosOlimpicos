from django.contrib import admin
from .models import Competicao, Resultado, Atleta, Modalidade

# Register your models here.
admin.site.register(Competicao)
admin.site.register(Resultado)
admin.site.register(Atleta)
admin.site.register(Modalidade)