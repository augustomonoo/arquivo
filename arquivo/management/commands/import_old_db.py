import json

from django.core.management.base import BaseCommand
from django.core.management.base import CommandError
from django.db.models import Model

from arquivo.models import Cliente
from arquivo.models import Documento
from arquivo.models import Historico
from arquivo.models import TipoDeDocumento
from django.contrib.auth import get_user_model

User = get_user_model()


# Tem problemas com timezones...
class Command(BaseCommand):
    help = "Importa o banco de dados do sistema antigo a partir de um json."

    def add_arguments(self, parser):
        parser.add_argument("arquivo_json", type=str)
        parser.add_argument("tabela_alvo", nargs="?", type=str)

    def _importar(self, klass, table: list[dict[str, str]]) -> None:
        self._criar_objs(klass, [klass(**c) for c in table])

    def _criar_objs(self, klass, objs: list[Model]):
        klass.objects.bulk_create(objs)

    def importar_usuario(self, table: list[dict[str, str]]) -> None:
        usuarios = [User(**c) for c in table]
        for u in usuarios:
            print(u.password, "->", end="")
            u.set_password(u.password)
            print(u.password)
        self._criar_objs(User, usuarios)

    def importar_historico(self, table: list[dict[str, str]]) -> None:
        self._importar(Historico, table)

    def importar_cliente(self, table: list[dict[str, str]]) -> None:
        self._importar(Cliente, table)

    def importar_tipodocumento(self, table: list[dict[str, str]]) -> None:
        self._importar(TipoDeDocumento, table)

    def importar_documento(self, table: list[dict[str, str]]) -> None:
        self._importar(Documento, table)

    def handle(self, *args, **options):
        if User.objects.count() != 1 or User.objects.first().id != 1:
            raise CommandError(
                f"É necessário ter apenas um usuário no banco de dados. Esse usuário deve ter id=1."
            )

        file_path = options["arquivo_json"]
        with open(file_path, "r") as f:
            old_database = json.loads(f.read())
            tabela_usuarios = old_database["FIN_FUNCIONARIOS.sql"]
            tabela_historico = old_database["CON_EVENTO.sql"]
            tabela_clientes = old_database["FIN_CLIENTES.sql"]
            tabela_tipo_doc = old_database["CAD_DESCRICAO.sql"]
            tabela_documentos = old_database["LAN_LANCAMENTO.sql"]

        # Options para importar tabela individual. Se omisso importa tudo
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
