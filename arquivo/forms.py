from abc import abstractmethod
from dataclasses import field
from django import forms
from arquivo.models import Arquivo, Documento
from django.db.models import QuerySet, Q


class ArquivoForm(forms.ModelForm):
    class Meta:
        model = Arquivo
        fields = "__all__"

    def save(self, *args, **kwargs) -> Arquivo:
        return super().save(*args, **kwargs)


class ConsultaBaseForm(forms.Form):
    termos = forms.CharField(max_length=255)

    # lista de tuplas (campo, operador)
    # campo: nome do campo no modelo (atual ou relacionado)
    # operador: "icontains", "iexact", etc
    campos_de_pesquisa = []

    def search(self, queryset: QuerySet) -> QuerySet:
        termos = self.cleaned_data["termos"]
        termos = termos.split()
        q = Q()
        for termo in termos:
            for campo, operador in self.campos_de_pesquisa:
                q = q | Q(**{f"{campo}__{operador}": termo})
        return queryset.filter(q)

    @abstractmethod
    def get_campos_de_pesquisa(self):
        return self.campos_de_pesquisa


class ConsultaDocumentoForm(ConsultaBaseForm):
    campos_de_pesquisa = [
        ("conteudo", "icontains"),
        ("cliente__razao_social", "icontains"),
    ]


class DocumentoForm(forms.ModelForm):
    class Meta:
        model = Documento
        fields = [
            "cliente",
            "tipo_de_documento",
            "conteudo",
        ]


class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ["nome"]
