from django.db import models
from django.urls import reverse_lazy


from django.contrib.auth.models import User

from .cliente import Cliente
from .tipo_de_documento import TipoDeDocumento


class Documento(models.Model):
    numero_caixa = models.FloatField(default=-1.0)
    tipo_de_documento = models.ForeignKey(
        TipoDeDocumento,
        verbose_name="tipo de documento",
        on_delete=models.DO_NOTHING,
    )
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING, null=True)
    data_finalizacao = models.DateTimeField(null=True)
    data_saida = models.DateTimeField(null=True)
    cliente = models.ForeignKey(
        Cliente, verbose_name="cliente", on_delete=models.DO_NOTHING
    )
    observacao = models.CharField(max_length=230, null=True)
    cheia = models.BooleanField(default=False)
    data_arquivo = models.DateTimeField(null=True)
    data_inicio = models.DateTimeField(null=True)

    class Meta:
        verbose_name = "documento"
        verbose_name_plural = "documentos"
        ordering = ["-data_arquivo"]

    def __str__(self):
        return f"{self.tipo_de_documento} - {self.observacao}"

    @classmethod
    def get_listar_url(cls):
        return reverse_lazy("documento_listar")
