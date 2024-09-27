from abc import abstractmethod
from dataclasses import field

from django import forms
from django.db.models import Q, QuerySet

from arquivo.models import Cliente, Documento
from arquivo.models.tipo_de_documento import TipoDeDocumento


class ConsultaBaseForm(forms.Form):
    s = forms.CharField(max_length=255, required=False)

    # lista de tuplas (campo, operador)
    # campo: nome do campo no modelo (atual ou relacionado)
    # operador: "icontains", "iexact", etc
    campos_de_pesquisa = []

    def search(self, queryset: QuerySet) -> QuerySet:
        s = self.cleaned_data["s"]
        s = s.split()
        q = Q()
        for termo in s:
            for campo, operador in self.campos_de_pesquisa:
                if operador == "exact" and not termo.isdigit():
                    continue
                q = q | Q(**{f"{campo}__{operador}": termo})
        return queryset.filter(q)

    @abstractmethod
    def get_campos_de_pesquisa(self):
        return self.campos_de_pesquisa


class ConsultaDocumentoForm(ConsultaBaseForm):
    campos_de_pesquisa = [
        ("observacao", "icontains"),
        ("cliente__razao_social", "icontains"),
        ("cliente__nome", "icontains"),
        ("numero_caixa", "exact"),
        ("tipo_de_documento__descricao", "icontains"),
    ]


class ImpressaoListaDocumentoForm(forms.Form):
    start_page = forms.IntegerField(label="Pagina inicial", min_value=1)
    end_page = forms.IntegerField(label="Pagina final", required=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["end_page"].initial = 0


class ConsultaClienteForm(ConsultaBaseForm):
    campos_de_pesquisa = [
        ("razao_social", "icontains"),
        ("nome", "icontains"),
        ("cnpj", "icontains"),
    ]


class DocumentoForm(forms.ModelForm):
    class Meta:
        model = Documento
        fields = [
            "cliente",
            "tipo_de_documento",
            "observacao",
            "data_finalizacao",
            "data_saida",
            # "data_arquivo",
            "data_inicio",
            "numero_caixa",
            "cheia",
        ]
        widgets = {
            "data_saida": forms.DateInput(attrs={"type": "date"}),
            "data_inicio": forms.DateInput(attrs={"type": "date"}),
            "data_finalizacao": forms.DateInput(attrs={"type": "date"}),
        }


class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        exclude = ["data_cadastro"]


class TipoDeDocumentoForm(forms.ModelForm):
    class Meta:
        model = TipoDeDocumento
        fields = "__all__"
