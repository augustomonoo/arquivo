from arquivo.models import Documento, Arquivo, TipoDeDocumento, Cliente


def arquivo(request):
    """Adiciona models do app ao context dos templates para buscar as urls deles"""
    return {
        "Arquivo": Arquivo,
        "Documento": Documento,
        "TipoDeDocumento": TipoDeDocumento,
        "Cliente": Cliente,
    }
