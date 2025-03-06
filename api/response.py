from typing import Any

from rest_framework import status
from rest_framework.response import Response


def response_ok_200(data: Any) -> Response:
    return Response(data, status=status.HTTP_200_OK)


def response_ok_201(data: Any) -> Response:
    return Response(data, status=status.HTTP_201_CREATED)


def response_error_400(data: Any) -> Response:
    return Response(data, status=status.HTTP_400_BAD_REQUEST)


def response_error_500(data: Any) -> Response:
    return Response(data, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


def response_error_500(msg: str = "") -> Response:
    return Response(f"Error Api {msg}", status=status.HTTP_500_INTERNAL_SERVER_ERROR)
