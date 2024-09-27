from dataclasses import dataclass, field

from django.http import HttpRequest, HttpResponse
from django.http.response import Http404
from django.shortcuts import get_list_or_404, render

from arquivo.forms import ConsultaDocumentoForm
from arquivo.models.documento import Documento


@dataclass
class Caixa:
    numero: int
    cheia: bool
    documentos: list[Documento] = field(default_factory=list)


def caixa_lista(request: HttpRequest) -> HttpResponse:
    caixas = [
        Caixa(numero=int(n), cheia=c)
        for n, c in Documento.objects.values_list("numero_caixa", "cheia").distinct()
    ]
    contexto = {
        "object_list": caixas,
        "caixas": caixas,
    }
    return render(request, "arquivo/caixa/listar.html", contexto)


def caixa_detalhe(request: HttpRequest, numero: int) -> HttpResponse:
    documentos = Documento.objects.filter(numero_caixa=numero)
    if documentos.count() == 0:
        raise Http404
    form = ConsultaDocumentoForm(request.GET or None)
    if form.is_valid():
        documentos = form.search(documentos)
    contexto = {
        "object_list": documentos,
        "form": form,
    }
    return render(request, "arquivo/documento/listar.html", contexto)
