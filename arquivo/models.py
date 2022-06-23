from django.db import models
from django.urls import reverse_lazy


class Cliente(models.Model):
    razao_social = models.CharField(max_length=512, verbose_name="razão social")

    def __str__(self) -> str:
        return self.razao_social


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


class TipoDeDocumento(models.Model):
    descricao = models.CharField(max_length=255, verbose_name="descrição")

    class Meta:
        verbose_name = "tipo de lançamento"
        verbose_name_plural = "tipo de lançamento"

    def __str__(self):
        return f"{self.descricao}"


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
