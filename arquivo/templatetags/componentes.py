from typing import NamedTuple, Optional

from django import template
from django.urls import reverse_lazy

from arquivo.models import Documento, Cliente

register = template.Library()


class NavLink(NamedTuple):
    text: str
    href: Optional[str] = None


@register.inclusion_tag("arquivo/componentes/menu.html")
def menu() -> dict[str, list[NavLink]]:
    return {
        "nav_links": [
            NavLink(text="Início", href=reverse_lazy("main_index")),
            NavLink(text="Documentos"),
            NavLink(text="Consultar Documentos", href=Documento.get_listar_url()),
            NavLink(text="Novo Lançamento", href=Documento.get_criar_url()),
            # "Arquivos",
            # {"href": Arquivo.get_criar_url(), "text": "Novo Arquivo"},
            # {"href": Arquivo.get_listar_url(), "text": "Consultar arquivos"},
            NavLink(text="Clientes"),
            NavLink(text="Consultar Clientes", href=Cliente.get_listar_url()),
            NavLink(text="Novo Cliente", href=Cliente.get_criar_url()),
            NavLink(text="Conta"),  # TODO: trocar o link de logout para um formulario de logout
            NavLink(text="Sair", href=reverse_lazy("logout")),
        ],
    }
