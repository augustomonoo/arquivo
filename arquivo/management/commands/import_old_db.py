from django.core.management.base import BaseCommand
from django.core.management.base import CommandError


class Command(BaseCommand):
    help = "Importa o banco de dados do sistema antigo a partir de um json."

    def add_arguments(self, parser):
        parser.add_argument("arquivo_json", type=str)

    def handle(self, *args, **options):
        print(options["arquivo_json"])
