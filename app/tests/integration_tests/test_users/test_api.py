import pytest
from httpx import AsyncClient


@pytest.mark.parametrize("email,password,status_code", [
    ("testy@testy.com", "testy", 200),
    ("testy@testy.com", "tosty", 409),
    ("ivan@testy.com", "testytesty", 200),
    ("abcde", "nonuser", 422),
])
async def test_register_user(email, password, status_code, ac: AsyncClient):
    response = await ac.post("/api/v1/auth/register", json={
        "email": email,
        "password": password,
    })

    assert response.status_code == status_code


@pytest.mark.parametrize("email,password,status_code", [
    ("test@test.com", "test", 200),
    ("wrong@person.com", "booogy", 401),
])
async def test_login_user(email, password, status_code, ac: AsyncClient):
    response = await ac.post("/api/v1/auth/login", json={
        "email": email,
        "password": password,
    })

    assert response.status_code == status_code
