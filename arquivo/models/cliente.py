from django.db import models
from django.urls import reverse_lazy
from typing import Any


class Cliente(models.Model):
    class TipoDePessoaChoices(models.TextChoices):
        FISICA = "F", "Pessoa Física"
        JURIDICA = "J", "Pessoa Jurídica"

    data_cadastro = models.DateTimeField(null=True, auto_now_add=True)
    nome = models.CharField(max_length=120, null=True)
    telefone1 = models.CharField(max_length=16, null=True, blank=True)
    telefone_contato = models.CharField(max_length=30, null=True, blank=True)
    cep = models.CharField(max_length=9, null=True, blank=True)
    tipo_pessoa = models.CharField(
        max_length=1,
        choices=TipoDePessoaChoices.choices,
        default=TipoDePessoaChoices.FISICA,
    )
    cidade = models.CharField(max_length=30, null=True, blank=True)
    sigla_estado = models.CharField(max_length=2, null=True, blank=True)
    cnpj = models.CharField(max_length=20, null=True, blank=True)
    inscricao_estadual = models.CharField(max_length=20, null=True, blank=True)
    razao_social = models.CharField(
        max_length=512, verbose_name="razão social", null=True, blank=True
    )
    atividade = models.CharField(max_length=250, null=True, blank=True)
    endereco = models.CharField(max_length=60, null=True, blank=True)
    bairro = models.CharField(max_length=30, null=True, blank=True)

    class Meta:
        ordering = ["nome", "razao_social"]

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

    def get_edit_url(self):
        return reverse_lazy("cliente_editar", kwargs={"id": self.id})

    def get_document_list_url(self) -> str:
        return reverse_lazy("cliente_documentos", kwargs={"cliente_id": self.id})

    def get_document_create_url(self) -> str:
        return reverse_lazy("cliente_documento_novo", kwargs={"cliente_id": self.id})

    def get_dict_field(self) -> dict[str, Any]:
        fields = [f for f in self._meta.get_fields() if hasattr(f, "verbose_name")]
        return {f.verbose_name: f.value_from_object(self) for f in fields}

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
        [setattr(self, a, getattr(self, a).upper()) for a in attrs if getattr(self, a)]
        return super().save(*args, **kwargs)
