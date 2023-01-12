from django.db import models
from django.urls import reverse_lazy


class Cliente(models.Model):
    razao_social = models.CharField(max_length=512, verbose_name="razão social")

    def __str__(self) -> str:
        return f"{self.razao_social}"

    @classmethod
    def get_criar_url(cls) -> str:
        return reverse_lazy("cliente_novo")
