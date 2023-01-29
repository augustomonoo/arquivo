from django.urls import include
from django.urls import path

from arquivo.views import cliente
from arquivo.views import documento
from arquivo.views import main


cliente_patterns = [
    path("", cliente.cliente_listar, name="cliente_listar"),
    path("<int:pk>/", cliente.cliente_detalhe, name="cliente_detalhe"),
    path("novo/", cliente.cliente_novo, name="cliente_novo"),
]

documento_patterns = [
    path("", documento.listar, name="documento_listar"),
    path("novo/", documento.novo, name="documento_novo"),
]

main_patterns = [
    path("", main.index, name="main_index"),
]

urlpatterns = [
    path("", include(main_patterns)),
    path("documento/", include(documento_patterns)),
    path("cliente/", include(cliente_patterns)),
]
