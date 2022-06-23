from django.shortcuts import render
from django.http import HttpResponse

from arquivo.forms import ConsultaDocumentoForm
from arquivo.models import Documento


def consulta(request) -> HttpResponse:
    form = ConsultaDocumentoForm(request.GET or None)
    queryset = Documento.objects.all()
    if form.is_valid():
        queryset = form.search(queryset)
    contexto = {
        "form": form,
        "queryset": queryset,
    }
    return render(request, "arquivo/main/consulta.html", contexto)
