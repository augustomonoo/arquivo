from .cliente import Cliente
from .tipo_de_documento import TipoDeDocumento
from django.db import models
from django.urls import reverse_lazy


class Documento(models.Model):
    cliente = models.ForeignKey(
        Cliente, verbose_name="cliente", on_delete=models.PROTECT
    )
    tipo_de_documento = models.ForeignKey(
        TipoDeDocumento,
        verbose_name="tipo de documento",
        on_delete=models.PROTECT,
    )
    conteudo = models.TextField(verbose_name="conteúdo")
    criado_em = models.DateTimeField(auto_now_add=True, verbose_name="criado em")
    modificado_em = models.DateTimeField(
        auto_now=True, verbose_name="ultima modificação"
    )

    class Meta:
        verbose_name = "documento"
        verbose_name_plural = "documentos"

    def __str__(self):
        return f"{self.arquivo} - {self.tipo_de_documento}"

    @classmethod
    def get_listar_url(cls):
        return reverse_lazy("documento_listar")
