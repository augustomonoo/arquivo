from typing import NamedTuple, Optional

from django import template
from django.urls import reverse_lazy

from arquivo.models import Documento, Cliente

register = template.Library()


class ComponenteRef(str):
    pass

class HRef(str):
    pass


class NavLink(NamedTuple):
    text: str
    action: Optional[HRef | ComponenteRef] = None

    def href(self) -> Optional[HRef]:
        return self.action

    def is_form(self) -> bool:
        match self.action:
            case ComponenteRef(_):
                return True
            case _:
                return False

    def is_link(self) -> bool:
        match self.action:
            case HRef(_):
                return True
            case _:
                return False


@register.inclusion_tag("arquivo/componentes/menu.html")
def menu() -> dict[str, list[NavLink]]:
    return {
        "nav_links": [
            NavLink(text="Início", action=HRef(reverse_lazy("main_index"))),
            NavLink(text="Documentos"),
            NavLink(text="Consultar Documentos", action=HRef(Documento.get_listar_url())),
            # "Arquivos",
            # {"href": Arquivo.get_criar_url(), "text": "Novo Arquivo"},
            # {"href": Arquivo.get_listar_url(), "text": "Consultar arquivos"},
            NavLink(text="Clientes"),
            NavLink(text="Consultar Clientes", action=HRef(Cliente.get_listar_url())),
            NavLink(text="Novo Cliente", action=HRef(Cliente.get_criar_url())),
            NavLink(text="Conta"),
            NavLink(text="Sair", action=ComponenteRef("arquivo/componentes/form_logout.html")),
        ],
    }
