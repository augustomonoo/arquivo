from typing import NamedTuple, Optional

from django import template
from django.urls import reverse_lazy

from arquivo.models import Documento, Cliente

register = template.Library()


class HRef(str):
    pass


class NavLink(NamedTuple):
    text: str
    action: Optional[HRef] = None

    def href(self) -> Optional[HRef]:
        return self.action

    def is_link(self) -> bool:
        return self.action is not None


@register.inclusion_tag("arquivo/componentes/menu.html")
def menu() -> dict[str, list[NavLink]]:
    return {
        "nav_links": [
            NavLink(text="Início", action=HRef(reverse_lazy("main_index"))),
            NavLink(text="Documentos"),
            NavLink(text="Consultar Documentos", action=HRef(Documento.get_listar_url())),
            NavLink(text="Novo Lançamento", action=HRef(Documento.get_criar_url())),
            # "Arquivos",
            # {"href": Arquivo.get_criar_url(), "text": "Novo Arquivo"},
            # {"href": Arquivo.get_listar_url(), "text": "Consultar arquivos"},
            NavLink(text="Clientes"),
            NavLink(text="Consultar Clientes", action=HRef(Cliente.get_listar_url())),
            NavLink(text="Novo Cliente", action=HRef(Cliente.get_criar_url())),
            NavLink(text="Conta"),  # TODO: trocar o link de logout para um formulario de logout
            NavLink(text="Sair", action=HRef(reverse_lazy("logout"))),
        ],
    }
