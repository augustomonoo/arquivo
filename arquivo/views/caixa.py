from django.http import HttpRequest, HttpResponse
from django.http.response import Http404
from django.shortcuts import render

from arquivo.forms import ConsultaDocumentoForm
from arquivo.models.documento import Documento
from arquivo.models.caixa import Caixa


def caixa_lista(request: HttpRequest) -> HttpResponse:
    qs = Documento.objects.all()
    form = ConsultaDocumentoForm(request.GET or None)
    if form.is_valid():
        qs = form.search(qs)
    caixas = [
        Caixa(numero=n, cheia=c)
        for n, c in qs.values_list("numero_caixa", "cheia").distinct()
    ]
    contexto = {
        "object_list": caixas,
        "caixas": caixas,
        "form": form,
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

def caixa_none(request: HttpRequest) -> HttpResponse:
    documentos = Documento.objects.filter(numero_caixa=None)
    form = ConsultaDocumentoForm(request.GET or None)
    if form.is_valid():
        documentos = form.search(documentos)
    contexto = {
        "object_list": documentos,
        "form": form,
    }
    return render(request, "arquivo/documento/listar.html", contexto)

