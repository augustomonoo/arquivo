from django.db import models
from arquivo.models import Arquivo, TipoDeDocumento, Cliente


class Documento(models.Model):
    arquivo = models.ForeignKey(
        Arquivo, verbose_name="arquivo", on_delete=models.PROTECT
    )
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
