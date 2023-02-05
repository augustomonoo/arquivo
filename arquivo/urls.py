from django.urls import include
from django.urls import path

from arquivo.views import cliente
from arquivo.views import documento
from arquivo.views import main


cliente_patterns = [
    path("", cliente.cliente_listar, name="cliente_listar"),
    path("<int:pk>/", cliente.cliente_detalhe, name="cliente_detalhe"),
    path("<int:id>/editar/", cliente.cliente_novo, name="cliente_editar"),
    path("<int:cliente_id>/documentos/", documento.listar, name="cliente_documentos"),
    path("novo/", cliente.cliente_novo, name="cliente_novo"),
]

documento_patterns = [
    path("", documento.listar, name="documento_listar"),
    path("imprimir/", documento.imprimir_lista, name="documento_imprimir_lista"),
    path("novo/", documento.novo, name="documento_novo"),
    path("<int:id>/", documento.detalhe, name="documento_detalhe"),
    path("<int:id>/editar/", documento.novo, name="documento_editar"),
]

main_patterns = [
    path("", main.index, name="main_index"),
]

urlpatterns = [
    path("", include(main_patterns)),
    path("documento/", include(documento_patterns)),
    path("cliente/", include(cliente_patterns)),
]
