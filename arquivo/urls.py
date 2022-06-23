from django.urls import path, include

from arquivo.views import arquivo
from arquivo.views import main
from arquivo.views import documento

documento_patterns = [
    path("", documento.listar, name="documento_listar"),
]

arquivo_patterns = [
    path("", arquivo.arquivo_listar, name="arquivo_listar"),
    path("novo/", arquivo.arquivo_novo, name="arquivo_novo"),
    path("<int:arquivo_id>/editar/", arquivo.arquivo_editar, name="arquivo_editar"),
    path(
        "<int:arquivo_id>/adicionar-documento/",
        arquivo.arquivo_adicionar_documento,
        name="arquivo_adicionar_documento",
    ),
]

main_patterns = [
    path("", main.index, name="main_index"),
]

urlpatterns = [
    path("", include(main_patterns)),
    path("documento/", include(documento_patterns)),
    path("arquivo/", include(arquivo_patterns)),
]
