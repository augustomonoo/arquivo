from typing import Any
from django.core.paginator import Paginator


def paginate(queryset, page_size: int = 25, page_number: int = 1) -> dict[str, Any]:
    paginator = Paginator(queryset, page_size)
    page = paginator.get_page(page_number)
    return {
        "object_list": page.object_list,
        "paginator": paginator,
        "page_obj": page,
    }
