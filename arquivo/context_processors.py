from arquivo.models import Cliente
from arquivo.models import Documento
from arquivo.models import TipoDeDocumento
from django.urls import reverse_lazy


def nav_links(request) -> dict:
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


def paginator_get_str(request) -> str:
    arguments = (
        {k: v for k, v in request.GET.items() if k != "page"} if request.GET else {}
    )
    return (
        ("&".join(["=".join([k, v]) for k, v in arguments.items()]) + "&")
        if arguments
        else ""
    )


def paginator_get(request) -> dict:
    return {k: v for k, v in request.GET.items() if k != "page"} if request.GET else {}


def arquivo(request) -> dict:
    """Contexto usado por todas as views na aplicação"""
    return {
        # "Arquivo": Arquivo,
        "Documento": Documento,
        "TipoDeDocumento": TipoDeDocumento,
        "Cliente": Cliente,
        **nav_links(request),
        "paginator_get_str": paginator_get_str(request),
        "paginator_get": paginator_get(request),
    }
