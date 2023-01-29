from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import render

from arquivo.forms import ConsultaDocumentoForm
from arquivo.forms import DocumentoForm
from arquivo.models import Documento
from arquivo.views.utils import paginate


def novo(request) -> HttpResponse:
    form = DocumentoForm(request.POST or None)
    if form.is_valid():
        documento = form.save(commit=False)
        documento.user = request.user
        # Sincronizar o estado da caixa com outros documentos que usam o mesmo
        # numero de caixa
        documento.save()
        return redirect(documento.get_editar_url())
    contexto = {
        "Documento": Documento,
        "form": form,
    }
    return render(request, "arquivo/documento/novo.html", contexto)


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
