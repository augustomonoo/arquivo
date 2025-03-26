from django.urls import include, path

from arquivo.views import caixa, cliente, documento, main

caixa_patterns = [
    path("", caixa.caixa_lista, name="caixa_lista"),
    path("<int:numero>", caixa.caixa_detalhe, name="caixa_detalhe"),
    path("sn", caixa.caixa_none, name="caixa_none"),
]

cliente_patterns = [
    path("", cliente.cliente_listar, name="cliente_listar"),
    path("<int:pk>/", cliente.cliente_detalhe, name="cliente_detalhe"),
    path("<int:pk>/_detalhe/", cliente.cliente_detalhe_partial, name="cliente_detalhe_partial"),
    path("<int:id>/editar/", cliente.cliente_novo, name="cliente_editar"),
    path("<int:cliente_id>/documentos/", documento.listar, name="cliente_documentos"),
    path("<int:cliente_id>/documentos_partial/", documento.listar_partial, name="cliente_documentos_partial"),
    path(
        "<int:cliente_id>/documentos/imprimir/",
        documento.imprimir_lista,
        name="cliente_imprimir_documentos",
    ),
    path("<int:cliente_id>/documentos/novo/", documento.novo, name="cliente_documento_novo"),
    path("<int:cliente_id>/documentos/<int:id>/", documento.detalhe, name="cliente_documento_detalhe"),
    path("<int:cliente_id>/documentos/<int:id>/editar/", documento.novo, name="cliente_documento_editar"),
    path("novo/", cliente.cliente_novo, name="cliente_novo"),
]

documento_patterns = [
    path("imprimir/", documento.imprimir_lista, name="documento_imprimir_lista"),
    path("novo_tipo/", documento.tipo_documento_novo, name="tipo_de_documento_novo"),
]

main_patterns = [
    path("", main.index, name="main_index"),
]

urlpatterns = [
    path("", include(main_patterns)),
    path("documento/", include(documento_patterns)),
    path("cliente/", include(cliente_patterns)),
    path("caixa/", include(caixa_patterns)),
]
