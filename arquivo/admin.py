from django.contrib import admin

from arquivo.models import Arquivo, Cliente, Documento, TipoDeDocumento


@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    pass


@admin.register(Arquivo)
class ArquivoAdmin(admin.ModelAdmin):
    pass


@admin.register(TipoDeDocumento)
class TipoDeLancamentoAdmin(admin.ModelAdmin):
    pass


@admin.register(Documento)
class LancamentoAdmin(admin.ModelAdmin):
    pass
