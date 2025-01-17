from rest_framework.pagination import PageNumberPagination


def create_pagination_class(
    page_size: int = 10,
    page_size_query_param: str = 'page_size',
    max_page_size: int = 100,
    invalid_page_message: str = 'Invalid page.'
):
    """
    Dynamically creates a pagination class with custom settings.

    Args:
        page_size (int): Default number of items per page.
        page_size_query_param (str): Query parameter name for page size.
        max_page_size (int): Maximum number of items per page.
        invalid_page_message (str): Error message for invalid pages.

    Returns:
        type: A dynamically created pagination class.
    """
    class CustomPagination(PageNumberPagination):
        def __init__(self):
            self.page_size = page_size
            self.page_size_query_param = page_size_query_param
            self.max_page_size = max_page_size
            self.invalid_page_message = invalid_page_message

    return CustomPagination
