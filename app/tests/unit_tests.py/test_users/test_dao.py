import pytest

from app.users.dao import UsersDAO


@pytest.mark.parametrize('email, exists', [
    ('test@test.com', True),
    ('ivan@example.com', True),
    ('boogy@test.com', False)
])
async def test_find_one_or_none(email, exists):
    user = await UsersDAO.find_one_or_none(email=email)
    
    if exists:
        assert user['email'] == email
    else:
        assert not user
