from django.db import models

from django.contrib.auth.models import User


class Historico(models.Model):
    """
    Gerado e gerenciado automaticamente, nao pode ser alterado por usuarios.
    """

    user = models.ForeignKey(User, null=True, on_delete=models.DO_NOTHING)
    descricao = models.CharField(max_length=100)
    data = models.DateTimeField(auto_now_add=True)
    formulario = models.CharField(max_length=80)  # qual aba gerou isso
    # copia do nome do usuario que gerou o historico
    nome_user = models.CharField(max_length=80, blank=True)
    complemento = models.CharField(max_length=240, null=True, blank=True)
