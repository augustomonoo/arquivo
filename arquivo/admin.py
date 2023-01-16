from django.contrib import admin

from arquivo.models import Cliente
from arquivo.models import Documento
from arquivo.models import TipoDeDocumento


@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    pass


@admin.register(TipoDeDocumento)
class TipoDeLancamentoAdmin(admin.ModelAdmin):
    pass


@admin.register(Documento)
class LancamentoAdmin(admin.ModelAdmin):
    pass
