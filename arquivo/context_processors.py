from arquivo.models import Cliente, Documento, TipoDeDocumento


def paginator_get_str(request) -> str:
    arguments = (
        {k: v for k, v in request.GET.items() if k != "page"} if request.GET else {}
    )
    return (
        ("&".join(["=".join([k, v]) for k, v in arguments.items()]) + "&")
        if arguments
        else ""
    )


def paginator_get(request) -> dict:
    return {k: v for k, v in request.GET.items() if k != "page"} if request.GET else {}


def arquivo(request) -> dict:
    """Contexto usado por todas as views na aplicação"""
    return {
        # "Arquivo": Arquivo,
        "Documento": Documento,
        "TipoDeDocumento": TipoDeDocumento,
        "Cliente": Cliente,
        "paginator_get_str": paginator_get_str(request),
        "paginator_get": paginator_get(request),
    }
