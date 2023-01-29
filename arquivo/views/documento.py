from django.shortcuts import render
from django.http import HttpResponse

from arquivo.forms import ConsultaDocumentoForm
from arquivo.models import Documento
from django.core.paginator import Paginator


def listar(request) -> HttpResponse:
    form = ConsultaDocumentoForm(request.GET or None)
    queryset = Documento.objects.all()
    if form.is_valid():
        queryset = form.search(queryset)
    paginator = Paginator(queryset, 10)
    page = paginator.get_page(request.GET.get("page", 1))
    contexto = {
        "form": form,
        "queryset": queryset,
        "object_list": page.object_list,
        "paginator": paginator,
        "page_obj": page,
    }
    return render(request, "arquivo/main/consulta.html", contexto)
