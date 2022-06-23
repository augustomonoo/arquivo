from django.db import models


class TipoDeDocumento(models.Model):
    descricao = models.CharField(max_length=255, verbose_name="descrição")

    class Meta:
        verbose_name = "tipo de lançamento"
        verbose_name_plural = "tipo de lançamento"

    def __str__(self):
        return f"{self.descricao}"
