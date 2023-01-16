from django.http import HttpResponse
from django.shortcuts import render

from arquivo.models import Documento


def index(request) -> HttpResponse:
    ultimos_lancamentos = Documento.objects.order_by("-data_arquivo")[:10]
    contexto = {"ultimos_lancamentos": ultimos_lancamentos}
    return render(request, "arquivo/main/index.html", contexto)
