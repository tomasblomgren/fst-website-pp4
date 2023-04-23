import pytest


def capital_case(x):
    return x.capitalize()


def test_capital_case():
    assert capital_case('semaphore') == 'Semaphore'


def test_raises_exception_on_non_string_arguments():
    with pytest.raises(TypeError):
        capital_case(9)


def capital_case(x):
    if not isinstance(x, str):
        raise TypeError('Please provide a string argument')
    return x.capitalize()


def test_user_logged_in(user):
    response = user.get('/profile')
    assert response.status_code == 200
    assert b'Welcome, username!' in response.data

# pytest pytest_bluedit/pytest-env/
