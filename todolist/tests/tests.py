import psycopg2
import pytest
import requests
from pytest_postgresql.executor import PostgreSQLExecutor


from core.serializers import RegistrationSerializer


def test_get_main_page():
    """Главная страница приложения работает"""
    response = requests.get("http://localhost/auth")
    assert response.status_code == 200


def test_get_vk_page():
    """Проверка входа на сайт через соцсеть VK"""
    response = requests.get("http://localhost/logged-in")
    assert response.status_code == 200


@pytest.mark.parametrize(
    "ctl_input, version",
    (
        ("pg_ctl (PostgreSQL) 10.18", "10.18"),
        ("pg_ctl (PostgreSQL) 11.13", "11.13"),
        ("pg_ctl (PostgreSQL) 12.8", "12.8"),
        ("pg_ctl (PostgreSQL) 13.4", "13.4"),
        ("pg_ctl (PostgreSQL) 14.0", "14.0"),
        ("pg_ctl (PostgreSQL) 15.1", "15.1"),
    ),
)
def test_versions(ctl_input: str, version: str) -> None:
    """Проверка корректности версий через регулярные варажения"""
    match = PostgreSQLExecutor.VERSION_RE.search(ctl_input)
    assert match is not None
    assert match.groupdict()["version"] == version


def test_bad_password():
    if RegistrationSerializer.validate:
        assert "Пароли совпадают!"


def test_new():
    try:
        conn = psycopg2.connect("dbname='postgres' user='postgres' password='postgres'")
    except:
        print("Don't connect to DB!")

    cur = conn.cursor()

    try:
        userrss = []
        cur.execute("SELECT username FROM core_user")
        for row in cur:
            userrss.append(row)

    except:
        print("No data!")
    print(str(userrss))
