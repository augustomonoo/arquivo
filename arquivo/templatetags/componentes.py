from django import template
from django.urls import reverse_lazy
from arquivo.models import Documento, Cliente

register = template.Library()

@register.inclusion_tag("arquivo/componentes/menu.html")
def menu() -> dict:
    return {
        "nav_links": (
            {"href": reverse_lazy("main_index"), "text": "Início"},
            "Documentos",
            {"href": Documento.get_listar_url(), "text": "Consultar documentos"},
            {"href": Documento.get_criar_url(), "text": "Novo Lançamento"},
            # "Arquivos",
            # {"href": Arquivo.get_criar_url(), "text": "Novo Arquivo"},
            # {"href": Arquivo.get_listar_url(), "text": "Consultar arquivos"},
            "Clientes",
            {"href": Cliente.get_listar_url(), "text": "Consultar clientes"},
            {"href": Cliente.get_criar_url(), "text": "Novo Cliente"},
            "Conta",
            {"href": reverse_lazy("logout"), "text": "Sair"},
        ),
    }
