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


class ConsultaForm(forms.Form):
    termos = forms.CharField(max_length=255)

    def search(self, queryset: QuerySet) -> QuerySet:
        termos = self.cleaned_data["termos"]
        termos = termos.split()
        for termo in termos:
            queryset = queryset.filter(Q(conteudo__icontains=termo))
        return queryset


class DocumentoForm(forms.ModelForm):
    class Meta:
        model = Documento
        fields = [
            "cliente",
            "tipo_de_documento",
            "conteudo",
        ]
