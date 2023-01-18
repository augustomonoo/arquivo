import json

from django.core.management.base import BaseCommand
from django.core.management.base import CommandError

from arquivo.models import Cliente
from arquivo.models import Documento
from arquivo.models import Historico
from arquivo.models import TipoDeDocumento
from django.contrib.auth.models import User


# Tem problemas com timezones...
class Command(BaseCommand):
    help = "Importa o banco de dados do sistema antigo a partir de um json."

    def add_arguments(self, parser):
        parser.add_argument("arquivo_json", type=str)
        parser.add_argument("tabela_alvo", nargs="?", type=str)

    def importar_usuario(self, table: list[dict[str, str]]) -> None:
        for usuario in table:
            print(usuario)
            User.objects.create_user(**usuario)

    def importar_historico(self, table: list[dict[str, str]]) -> None:
        entradas = [Historico(**c) for c in table]
        Historico.objects.bulk_create(entradas)

    def importar_cliente(self, table: list[dict[str, str]]) -> None:
        clientes = [Cliente(**c) for c in table]
        Cliente.objects.bulk_create(clientes)

    def importar_tipodocumento(self, table: list[dict[str, str]]) -> None:
        documentos = [TipoDeDocumento(**d) for d in table]
        TipoDeDocumento.objects.bulk_create(documentos)

    def importar_documento(self, table: list[dict[str, str]]) -> None:
        documentos = [Documento(**d) for d in table]
        Documento.objects.bulk_create(documentos)

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
                self.importar_usuario(tabela_usuarios)
            case "historico":
                self.importar_historico(tabela_historico)
            case "clientes":
                self.importar_cliente(tabela_clientes)
            case "tipo_de_documento":
                self.importar_tipodocumento(tabela_tipo_doc)
            case "documentos":
                self.importar_documento(tabela_documentos)
            case _:
                self.importar_usuario(tabela_usuarios)
                self.importar_tipodocumento(tabela_tipo_doc)
                self.importar_cliente(tabela_clientes)
                self.importar_documento(tabela_documentos)
                self.importar_historico(tabela_historico)
