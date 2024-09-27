from dataclasses import dataclass, field

from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from arquivo.models.documento import Documento


@dataclass
class Caixa:
    numero: int
    cheia: bool
    documentos: list[Documento] = field(default_factory=list)


def caixa_lista(request: HttpRequest) -> HttpResponse:
    caixas = [
        Caixa(numero=n, cheia=c)
        for n, c in Documento.objects.values_list("numero_caixa", "cheia").distinct()
    ]
    contexto = {
        "object_list": caixas,
        "caixas": caixas,
    }
    return render(request, "arquivo/caixa/listar.html", contexto)
