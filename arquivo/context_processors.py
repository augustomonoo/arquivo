from django.urls import reverse_lazy
from arquivo.models import Documento, Arquivo, TipoDeDocumento, Cliente


def nav_links(request) -> dict:
    return {
        "nav_links": (
            {"href": reverse_lazy("main_index"), "text": "Início"},
            "Documentos",
            {"href": Documento.get_listar_url(), "text": "Consultar documentos"},
            "Arquivo",
            {"href": Arquivo.get_criar_url(), "text": "Novo Arquivo"},
            {"href": Arquivo.get_listar_url(), "text": "Consultar arquivos"},
        ),
    }


def arquivo(request) -> dict:
    """Contexto usado por todas as views na aplicação"""
    return {
        "Arquivo": Arquivo,
        "Documento": Documento,
        "TipoDeDocumento": TipoDeDocumento,
        "Cliente": Cliente,
        **nav_links(request),
    }
