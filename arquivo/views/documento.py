from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from django.shortcuts import render

from arquivo.forms import ConsultaDocumentoForm
from arquivo.forms import DocumentoForm
from arquivo.models import Documento
from arquivo.models import Historico
from arquivo.views.utils import paginate


def novo(request, id: int = None) -> HttpResponse:
    form = DocumentoForm(
        request.POST or None, instance=Documento.objects.get(id=id) if id else None
    )
    if form.is_valid():
        documento = form.save(commit=False)
        if not id:
            documento.user = request.user
        documento.save()
        # Sincronizar o estado da caixa com outros documentos que usam o mesmo
        # numero de caixa
        Documento.objects.filter(numero_caixa=documento.numero_caixa).update(
            cheia=documento.cheia
        )
        historico = Historico(user=request.user, nome_user=request.user.get_full_name())
        historico.formulario = "editar documento" if id else "novo cliente"
        historico.descricao = f"id: {documento.id}"
        historico.save()
        return redirect(documento.get_detalhe_url())
    contexto = {
        "Documento": Documento,
        "form": form,
    }
    return render(request, "arquivo/documento/novo.html", contexto)


def detalhe(request, id: int) -> HttpResponse:
    documento = get_object_or_404(Documento, id=id)
    contexto = {
        "Documento": Documento,
        "documento": documento,
    }
    return render(request, "arquivo/documento/detalhe.html", contexto)


def listar(request, cliente_id: int = None) -> HttpResponse:
    form = ConsultaDocumentoForm(request.GET or None)
    if cliente_id:
        queryset = Documento.objects.filter(cliente_id=cliente_id)
    else:
        queryset = Documento.objects.all()
    if form.is_valid():
        queryset = form.search(queryset)
    contexto = {
        "form": form,
        "queryset": queryset,
        **paginate(queryset, page_number=request.GET.get("page")),
    }
    return render(request, "arquivo/main/consulta.html", contexto)
