from django.core.paginator import Paginator
from typing import Any


__PAGINATOR_DEFAULT_SIZE__: int = 25


def paginate(
    queryset, page_size: int = __PAGINATOR_DEFAULT_SIZE__, page_number: int = 1
) -> dict[str, Any]:
    paginator = Paginator(queryset, page_size)
    page = paginator.get_page(page_number)
    return {
        "object_list": page.object_list,
        "paginator": paginator,
        "page_obj": page,
    }


def get_range_objects(
    queryset,
    object_per_page: int = __PAGINATOR_DEFAULT_SIZE__,
    start_page: int = 1,
    end_page: int = None,
):
    """[start_page, end_page)
    indice inicial em 1
    """
    start = (start_page - 1) * object_per_page
    if end_page and end_page >= start_page:
        end = end_page * object_per_page
        return {"object_list": queryset[start:end]}
    return {"object_list": queryset[start:]}
