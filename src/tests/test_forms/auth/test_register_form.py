from forms.auth import RegisterForm
from tests.utils import form_data


def test_validates_proper_input() -> None:
    """
    Make sure that the form allows proper input
    """
    data = form_data(
        {
            "username": "username",
            "email": "email@email.com",
            "password": "Password_123",
            "password_confirmation": "Password_123",
        }
    )
    form = RegisterForm(formdata=data)

    assert form.validate()


def test_does_not_validate_too_short_username() -> None:
    """
    Make sure that the form does not allow a username shorter than 4 characters
    """
    data = form_data(
        {
            "username": "abc",
            "email": "email@email.com",
            "password": "Password_123",
            "password_confirmation": "Password_123",
        }
    )
    form = RegisterForm(formdata=data)

    assert not form.validate()


def test_does_not_validate_too_long_username() -> None:
    """
    Make sure that the form does not allow a username longer than 64 characters
    """
    data = form_data(
        {
            "username": "a" * 65,
            "email": "email@email.com",
            "password": "Password_123",
            "password_confirmation": "Password_123",
        }
    )
    form = RegisterForm(formdata=data)

    assert not form.validate()


def test_does_not_validate_invalid_email() -> None:
    """
    Make sure that the form does not allow an invalid email
    """
    data = form_data(
        {
            "username": "username",
            "email": "email.email.com",
            "password": "Password_123",
            "password_confirmation": "Password_123",
        }
    )
    form = RegisterForm(formdata=data)

    assert not form.validate()


def test_does_not_validate_too_short_password() -> None:
    """
    Make sure that the form does not allow a password with less than 8 characters
    """
    data = form_data(
        {
            "username": "username",
            "email": "email.email.com",
            "password": "passwor",
            "password_confirmation": "passwor",
        }
    )
    form = RegisterForm(formdata=data)

    assert not form.validate()


def test_does_not_validate_too_long_password() -> None:
    """
    Make sure that the form does not allow a password with more than 64 characters
    """
    data = form_data(
        {
            "username": "username",
            "email": "email.email.com",
            "password": "p" * 65,
            "password_confirmation": "p" * 65,
        }
    )
    form = RegisterForm(formdata=data)

    assert not form.validate()


def test_does_not_validate_password_with_no_lowercase_character() -> None:
    """
    Make sure that the form does not allow a password without a lowercase letter
    """
    data = form_data(
        {
            "username": "username",
            "email": "email.email.com",
            "password": "PASSWORD_123",
            "password_confirmation": "PASSWORD_123",
        }
    )
    form = RegisterForm(formdata=data)

    assert not form.validate()


def test_does_not_validate_password_with_no_uppercase_character() -> None:
    """
    Make sure that the form does not allow a password without an uppercase letter
    """
    data = form_data(
        {
            "username": "username",
            "email": "email.email.com",
            "password": "password_123",
            "password_confirmation": "password_123",
        }
    )
    form = RegisterForm(formdata=data)

    assert not form.validate()


def test_does_not_validate_password_without_digit() -> None:
    """
    Make sure that the form does not allow a password without a digit
    """
    data = form_data(
        {
            "username": "username",
            "email": "email.email.com",
            "password": "password_",
            "password_confirmation": "password_",
        }
    )
    form = RegisterForm(formdata=data)

    assert not form.validate()


def test_does_not_validate_password_with_no_special_character() -> None:
    """
    Make sure that the form does not allow a password without a special character
    """
    data = form_data(
        {
            "username": "username",
            "email": "email.email.com",
            "password": "password123",
            "password_confirmation": "password123",
        }
    )
    form = RegisterForm(formdata=data)

    assert not form.validate()


def test_does_not_validate_password_confirmation_that_doesnt_match_password() -> None:
    """
    Make sure that the form does not allow a password confirmation different from the password
    """
    data = form_data(
        {
            "username": "username",
            "email": "email.email.com",
            "password": "Password_123",
            "password_confirmation": "Password_1234",
        }
    )
    form = RegisterForm(formdata=data)

    assert not form.validate()
