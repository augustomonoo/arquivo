from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import render

from arquivo.forms import ConsultaDocumentoForm
from arquivo.models import Documento
from arquivo.views.utils import paginate


def listar(request) -> HttpResponse:
    form = ConsultaDocumentoForm(request.GET or None)
    queryset = Documento.objects.all()
    if form.is_valid():
        queryset = form.search(queryset)
    contexto = {
        "form": form,
        "queryset": queryset,
        **paginate(queryset, page_number=request.GET.get("page")),
    }
    return render(request, "arquivo/main/consulta.html", contexto)
