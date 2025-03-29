from dataclasses import dataclass, field
from .documento import Documento
from django.urls import reverse_lazy


@dataclass
class Caixa:
    numero: int | None
    cheia: bool
    documentos: list[Documento] = field(default_factory=list)

    def get_absolute_url(self) -> str:
        if self.numero:
            return reverse_lazy("caixa_detalhe", kwargs={"numero": self.numero})
        return reverse_lazy("caixa_none")
