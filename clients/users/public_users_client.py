
from typing import TypedDict

from httpx import Response

from clients.api_client import ApiClient

from clients.public_http_builder import get_public_http_client

class UserCreateRequestDict(TypedDict):
    """
    Описание структуры запроса на создание пользователя
    """
    email: str
    password: str
    lastName: str
    firstName: str

class PublicUsersClient(ApiClient):
    """
    Клиент для работы с /api/v1/users
    """
    def create_user_api(self, request: UserCreateRequestDict) -> Response:
        """
        Метод создает пользователя

        :param request: Словарь с email, password, lastName, firstName, middleName
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.post("/v1/users", json=request)

# Добавляем builder для PublicUsersClient
def get_public_users_client() -> PublicUsersClient:
    """
    Функция создаёт экземпляр PublicUsersClient с уже настроенным HTTP-клиентом.

    :return: Готовый к использованию PublicUsersClient.
    """
    return PublicUsersClient(client=get_public_http_client())
