from django.db import models
from django.urls import reverse_lazy


class Arquivo(models.Model):
    etiqueta = models.PositiveIntegerField(verbose_name="etiqueta", unique=True)
    fechado = models.BooleanField(verbose_name="fechado", default=False)

    def __str__(self) -> str:
        return f"{self.etiqueta:05}"

    def get_editar_url(self) -> str:
        return reverse_lazy("arquivo_editar", args=(self.id,))

    @classmethod
    def get_novo_url(self) -> str:
        return reverse_lazy("arquivo_novo")

    @classmethod
    def get_listar_url(self) -> str:
        return reverse_lazy("arquivo_listar")

    def get_adicionar_documento_url(self):
        return reverse_lazy("arquivo_adicionar_documento", args=(self.id,))
