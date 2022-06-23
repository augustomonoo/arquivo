from django.http import HttpResponse
from arquivo.models import Documento
from django.shortcuts import render
from arquivo.forms import ConsultaForm


def index(request) -> HttpResponse:
    ultimos_lancamentos = Documento.objects.order_by("-criado_em")[:10]
    contexto = {"ultimos_lancamentos": ultimos_lancamentos}
    return render(request, "arquivo/main/index.html", contexto)


def consulta(request) -> HttpResponse:
    form = ConsultaForm(request.GET or None)
    queryset = Documento.objects.all()
    if form.is_valid():
        queryset = form.search(queryset)
    contexto = {
        "form": form,
        "queryset": queryset,
    }
    return render(request, "arquivo/main/consulta.html", contexto)
