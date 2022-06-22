from django.db import models


class Cliente(models.Model):
    razao_social = models.CharField(max_length=512, verbose_name="razão social")

    def __str__(self) -> str:
        return self.razao_social


class Arquivo(models.Model):
    etiqueta = models.PositiveIntegerField(verbose_name="etiqueta", unique=True)
    fechado = models.BooleanField(verbose_name="fechado", default=False)

    def __str__(self) -> str:
        return f"{self.etiqueta:05}"


class TipoDeLancamento(models.Model):
    descricao = models.CharField(max_length=255, verbose_name="descrição")

    class Meta:
        verbose_name = "tipo de lançamento"
        verbose_name_plural = "tipo de lançamento"

    def __str__(self):
        return f"{self.descricao}"


class Lancamento(models.Model):
    arquivo = models.ForeignKey(
        "arquivo.Arquivo", verbose_name="arquivo", on_delete=models.PROTECT
    )
    cliente = models.ForeignKey(
        "arquivo.Cliente", verbose_name="cliente", on_delete=models.PROTECT
    )
    tipo_de_lancamento = models.ForeignKey(
        "arquivo.TipoDeLancamento",
        verbose_name="tipo de lançamento",
        on_delete=models.PROTECT,
    )
    conteudo = models.TextField(verbose_name="conteúdo")
    criado_em = models.DateTimeField(auto_now_add=True, verbose_name="criado em")
    modificado_em = models.DateTimeField(
        auto_now=True, verbose_name="ultima modificação"
    )

    class Meta:
        verbose_name = "lançamento"
        verbose_name_plural = "lançamentos"

    def __str__(self):
        return f"{self.arquivo} - {self.tipo_de_lancamento}"
