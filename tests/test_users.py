from http import HTTPStatus
import pytest
from tests.conftest import UserFixture
from clients.authentication.authentication_client import AuthenticationClient
from clients.users.public_users_client import PublicUsersClient
from clients.users.users_schema import CreateUserRequestSchema, CreateUserResponseSchema
# Импортируем функцию для валидации JSON Schema
from tools.assertions.schema import validate_json_schema
from tools.assertions.base import assert_status_code
from tools.assertions.users import assert_create_user_response

@pytest.mark.users
@pytest.mark.regression
def test_create_user(public_users_client: PublicUsersClient):

    request = CreateUserRequestSchema()
    response = public_users_client.create_user_api(request)

    response_data = CreateUserResponseSchema.model_validate_json(response.text)

    # Используем функцию для проверки статус-кода
    assert_status_code(response.status_code, HTTPStatus.OK)
    # Используем функцию для проверки ответа создания юзера
    assert_create_user_response(request, response_data)

    # Проверяем, что тело ответа соответствует ожидаемой JSON-схеме
    validate_json_schema(response.json(), response_data.model_json_schema())

@pytest.mark.users
@pytest.mark.regression
def test_get_user_me(function_user: UserFixture,
               authentication_client: AuthenticationClient):

    # Выполнить запрос

    # Запрос на логин (login_request -> request)
    request = LoginRequestSchema(email=function_user.email, password=function_user.password)

    private_users_client = get_private_users_client(request)

    get_user_response = private_users_client.get_user(create_user_response.user.id)

    # Выполнить проверки