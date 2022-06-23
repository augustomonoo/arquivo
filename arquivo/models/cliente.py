from django.db import models


class Cliente(models.Model):
    razao_social = models.CharField(max_length=512, verbose_name="razão social")

    def __str__(self) -> str:
        return self.razao_social
