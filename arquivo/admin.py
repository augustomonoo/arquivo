from django.contrib import admin

from arquivo.models import Arquivo, Cliente, Lancamento, TipoDeLancamento


@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    pass


@admin.register(Arquivo)
class ArquivoAdmin(admin.ModelAdmin):
    pass


@admin.register(TipoDeLancamento)
class TipoDeLancamentoAdmin(admin.ModelAdmin):
    pass


@admin.register(Lancamento)
class LancamentoAdmin(admin.ModelAdmin):
    pass
