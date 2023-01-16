from django.db import models
from django.urls import reverse_lazy

from .arquivo import Arquivo  # remover
from .cliente import Cliente  # fin_clientes
from .documento import Documento  # lan_lancaamento
from .tipo_de_documento import TipoDeDocumento  # cad_descricao

# from .historico import Historico  # con_evento
