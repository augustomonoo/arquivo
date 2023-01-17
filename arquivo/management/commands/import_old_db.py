import json

from django.core.management.base import BaseCommand
from django.core.management.base import CommandError


class Command(BaseCommand):
    help = "Importa o banco de dados do sistema antigo a partir de um json."

    def add_arguments(self, parser):
        parser.add_argument("arquivo_json", type=str)
        parser.add_argument("tabela_alvo", type=str)

    def importar_usuario(self, table: list[dict[str, str]]) -> None:
        pass

    def importar_historico(self, table: list[dict[str, str]]) -> None:
        pass

    def importar_cliente(self, table: list[dict[str, str]]) -> None:
        pass

    def importar_tipodocumento(self, table: list[dict[str, str]]) -> None:
        pass

    def importar_documento(self, table: list[dict[str, str]]) -> None:
        pass

    def handle(self, *args, **options):
        file_path = options["arquivo_json"]
        with open(file_path, "r") as f:
            old_database = json.loads(f.read())
            tabela_usuarios = old_database["FIN_FUNCIONARIOS.sql"]
            tabela_historico = old_database["CON_EVENTO.sql"]
            tabela_clientes = old_database["FIN_CLIENTES.sql"]
            tabela_tipo_doc = old_database["CAD_DESCRICAO.sql"]
            tabela_documentos = old_database["LAN_LANCAMENTO.sql"]
        match options.get("tabela_alvo", None):
            case "usuarios":
                importar_usuario(tabela_usuarios)
            case "historico":
                importar_historico(tabela_historico)
            case "cliente":
                importar_cliente(tabela_clientes)
            case "tipo_de_documento":
                importar_tipodocumento(tabela_tipo_doc)
            case "documento":
                importar_documento(tabela_documentos)
            case _:
                importar_usuario(tabela_usuarios)
                importar_historico(tabela_historico)
                importar_cliente(tabela_clientes)
                importar_tipodocumento(tabela_tipo_doc)
                importar_documento(tabela_documentos)
