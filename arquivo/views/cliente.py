from audioop import reverse
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from arquivo.forms import ClienteForm
from arquivo.models import Cliente


def cliente_novo(request) -> HttpResponse:
    form = ClienteForm(request.POST or None)
    if form.is_valid():
        cliente = form.save()
        return redirect(cliente.get_editar_url())
    contexto = {
        "Cliente": Cliente,
        "form": form,
    }
    return render(request, "arquivo/cliente/novo.html", contexto)
