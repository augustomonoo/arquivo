from django.db import models
from django.urls import reverse_lazy
from django.utils import timezone

from typing import Any


from django.contrib.auth.models import User

from .cliente import Cliente
from .tipo_de_documento import TipoDeDocumento


class Documento(models.Model):
    numero_caixa = models.PositiveIntegerField(blank=True, null=True)
    tipo_de_documento = models.ForeignKey(
        TipoDeDocumento,
        verbose_name="tipo de documento",
        on_delete=models.DO_NOTHING,
    )
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING, null=True)
    data_finalizacao = models.DateTimeField(null=True, blank=True)
    data_saida = models.DateTimeField(null=True, blank=True)
    cliente = models.ForeignKey(
        Cliente, verbose_name="cliente", on_delete=models.DO_NOTHING
    )
    observacao = models.CharField(max_length=230, null=True, blank=True)
    cheia = models.BooleanField(default=False)
    data_arquivo = models.DateTimeField(null=True, blank=True, default=timezone.now)
    data_inicio = models.DateTimeField(null=True, blank=True)

    class Meta:
        verbose_name = "documento"
        verbose_name_plural = "documentos"
        ordering = ["-data_arquivo"]

    def __str__(self):
        return f"{self.tipo_de_documento} - {self.observacao}"

    @classmethod
    def get_listar_url(cls):
        return reverse_lazy("documento_listar")

    @classmethod
    def get_criar_url(cls) -> str:
        return reverse_lazy("documento_novo")

    def get_absolute_url(self) -> str:
        return reverse_lazy("documento_detalhe", kwargs={"id": self.id})

    def get_edit_url(self):
        return reverse_lazy("documento_editar", kwargs={"id": self.id})

    def get_detalhe_url(self) -> str:
        return self.get_absolute_url()

    def get_dict_field(self) -> dict[str, Any]:
        fields = [f for f in self._meta.get_fields() if hasattr(f, "verbose_name")]
        return {f.verbose_name: f.value_from_object(self) for f in fields}
