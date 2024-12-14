from rest_framework import status
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.response import Response


def paginate_response():
    def decorator(func):
        def wrapper(self, request, *args, **kwargs):
            # Get the queryset from the decorated function
            queryset = func(self, request, *args, **kwargs)

            if kwargs.get("pk", None):
                serializer = self.serializer_class(queryset)
                return Response(serializer.data, status=status.HTTP_200_OK)

            paginator = LimitOffsetPagination()
            paginated_queryset = paginator.paginate_queryset(
                queryset, request, view=self
            )

            # Serialize paginated data
            serializer = self.serializer_class(paginated_queryset, many=True)
            return paginator.get_paginated_response(serializer.data)

        return wrapper

    return decorator
