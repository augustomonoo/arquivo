from audioop import reverse

from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render

from arquivo.forms import ClienteForm, ConsultaClienteForm
from arquivo.models import Cliente
from arquivo.views.utils import paginate


def cliente_listar(request) -> HttpResponse:
    queryset = Cliente.objects.all()
    form = ConsultaClienteForm(request.GET or None)
    if form.is_valid():
        queryset = form.search(queryset)
    contexto = {
        "Cliente": Cliente,
        "queryset": queryset,
        "form": form,
        **paginate(queryset, page_number=request.GET.get("page")),
    }
    return render(request, "arquivo/cliente/listar.html", contexto)


def cliente_detalhe(request, pk: int) -> HttpResponse:
    cliente = get_object_or_404(Cliente, pk=pk)
    contexto = {
        "Cliente": Cliente,
        "cliente": cliente,
    }
    return render(request, "arquivo/cliente/detalhe.html", contexto)


def cliente_novo(request, id: int = None) -> HttpResponse:
    form = ClienteForm(
        request.POST or None, instance=Cliente.objects.get(id=id) if id else None
    )
    if form.is_valid():
        cliente = form.save()
        return redirect(cliente.get_detalhe_url())
    contexto = {
        "Cliente": Cliente,
        "form": form,
    }
    return render(request, "arquivo/cliente/novo.html", contexto)
