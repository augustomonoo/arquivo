from django.db import models
from django.urls import reverse_lazy


class Cliente(models.Model):
    class TipoDePessoaChoices(models.TextChoices):
        FISICA = "F", "Pessoa Física"
        JURIDICA = "J", "Pessoa Jurídica"

    data_cadastro = models.DateTimeField(null=True, auto_now_add=True)
    nome = models.CharField(max_length=120, null=True)
    telefone1 = models.CharField(max_length=16, null=True)
    telefone_contato = models.CharField(max_length=30, null=True)
    cep = models.CharField(max_length=9, null=True)
    tipo_pessoa = models.CharField(
        max_length=1,
        choices=TipoDePessoaChoices.choices,
        default=TipoDePessoaChoices.FISICA,
    )
    cidade = models.CharField(max_length=30, null=True)
    sigla_estado = models.CharField(max_length=2, null=True)
    cnpj = models.CharField(max_length=20, null=True)
    inscricao_estadual = models.CharField(max_length=20, null=True)
    razao_social = models.CharField(
        max_length=512, verbose_name="razão social", null=True
    )
    atividade = models.CharField(max_length=250, null=True)
    endereco = models.CharField(max_length=60, null=True)
    bairro = models.CharField(max_length=30, null=True)

    def __str__(self) -> str:
        return f"{self.razao_social or self.nome}"

    @classmethod
    def get_criar_url(cls) -> str:
        return reverse_lazy("cliente_novo")

    @classmethod
    def get_listar_url(cls) -> str:
        return reverse_lazy("cliente_listar")

    def get_absolute_url(self):
        return reverse_lazy("cliente_detalhe", kwargs={"pk": self.pk})

    def get_detalhe_url(self):
        return self.get_absolute_url()

    def save(self, *args, **kwargs):
        attrs = (
            "nome",
            "cidade",
            "sigla_estado",
            "razao_social",
            "atividade",
            "endereco",
            "bairro",
        )
        for a in attrs:
            setattr(self, a, getattr(self, a).upper())
        return super().save(*args, **kwargs)
