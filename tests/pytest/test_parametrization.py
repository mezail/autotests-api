import pytest
from _pytest.fixtures import SubRequest

@pytest.mark.parametrize("number", [1, 2, 3, -1])  # Параметризируем тест
# Название "number" в декораторе "parametrize" и в аргументах автотеста должны совпадать
def test_numbers(number: int):
    assert number > 0


@pytest.mark.parametrize("number, expected", [(1, 1), (2, 4), (3, 9)])
# В данном случае в качестве данных используется список с кортежами
def test_several_numbers(number: int, expected: int):
    # Возводим число number в квадрат и проверяем, что оно равно ожидаемому
    assert number ** 2 == expected


@pytest.mark.parametrize("os", ["macos", "windows", "linux", "debian"])  # Параметризируем по операционной системе
@pytest.mark.parametrize("host", [
    "https://dev.company.com",
    "https://stable.company.com",
    "https://prod.company.com"
])  # Параметризируем по хосту
def test_multiplication_of_numbers(os: str, host: str):
    assert len(os + host) > 0  # Проверка указана для примера


@pytest.fixture(params=[
    "https://dev.company.com",
    "https://stable.company.com",
    "https://prod.company.com"
])
# Фикстура будет возвращать три разных хоста
# Соотвественно все автотесты использующие данную фикстуру будут запускаться три раза
def host(request: SubRequest) -> str:
    # Внутри атрибута param находится одно из значений "https://dev.company.com",
    # "https://stable.company.com", "https://prod.company.com"
    return request.param


# В самом автотесте уже не нужно добавлять параметризацию, он будет автоматически параметризован из фикстуры
def test_host(host: str):
    # Используем фикстуру в автотесте, она вернет нам хост в виде строки
    print(f"Running test on host: {host}")


# Для тестовых классов параметризация указывается для самого класса
@pytest.mark.parametrize("user", ["Alice", "Zara"])
class TestOperations:
    # Параметр "user" передается в качестве аргумента в каждый тестовый метод класса
    def test_user_with_operations(self, user: str):
        print(f"User with operations: {user}")

    # Аналогично тут передается "user"
    def test_user_without_operations(self, user: str):
        print(f"User without operations: {user}")

@pytest.mark.parametrize("user", ["Alice", "Zara"])
class TestOperations:
    @pytest.mark.parametrize("account", ["Credit card", "Debit card"])
    def test_user_with_operations(self, user: str, account: str):
        # Данный автотест будет запущен 4 раза
        print(f"User with operations: {user}")


# Словарь пользователей: номер телефона — ключ, описание — значение
users = {
    "+70000000011": "User with money on bank account",
    "+70000000022": "User without money on bank account",
    "+70000000033": "User with operations on bank account"
}

@pytest.mark.parametrize(
    "phone_number",
    users.keys(),  # Передаем список номеров телефонов
    ids=lambda phone_number: f"{phone_number}: {users[phone_number]}"  # Генерируем идентификаторы динамически
)
def test_identifiers(phone_number: str):
    pass