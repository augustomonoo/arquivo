from audioop import reverse
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from arquivo.forms import ArquivoForm, DocumentoForm
from arquivo.models import Documento, Arquivo


def arquivo_novo(request) -> HttpResponse:
    form = ArquivoForm(request.POST or None)
    if form.is_valid():
        arquivo = form.save()
        return redirect(arquivo.get_editar_url())
    contexto = {
        "Arquivo": Arquivo,
        "form": form,
    }
    return render(request, "arquivo/arquivo/novo.html", contexto)


def arquivo_editar(request, arquivo_id: int) -> HttpResponse:
    arquivo = get_object_or_404(Arquivo, id=arquivo_id)
    form = ArquivoForm(request.POST or None, instance=arquivo)
    if form.is_valid():
        arquivo = form.save()
        return redirect(arquivo.get_editar_url())
    contexto = {
        "Arquivo": Arquivo,
        "form": form,
    }
    return render(request, "arquivo/arquivo/novo.html", contexto)


def arquivo_listar(request) -> HttpResponse:
    arquivos = Arquivo.objects.all()
    contexto = {"arquivos": arquivos}
    return render(request, "arquivo/arquivo/listar.html", contexto)


def arquivo_adicionar_documento(request, arquivo_id: int) -> HttpResponse:
    arquivo = get_object_or_404(Arquivo, id=arquivo_id)
    form = DocumentoForm(request.POST or None)
    if form.is_valid():
        documento = form.save(commit=False)
        documento.arquivo = arquivo
        documento.save()
        return redirect(arquivo.get_editar_url())
    contexto = {
        "Arquivo": Arquivo,
        "arquivo": arquivo,
        "form": form,
    }
    return render(request, "arquivo/arquivo/novo.html", contexto)
