from forms.auth import RegisterForm


def test_validates_proper_input(form_data_factory) -> None:
    """
    Make sure that the form allows proper input

    :param form_data_factory: A factory for form data dictionaries
    """
    form_data = form_data_factory(
        {
            "username": "username",
            "email": "email@email.com",
            "password": "Password_123",
            "password_confirmation": "Password_123",
        }
    )
    form = RegisterForm(formdata=form_data)

    assert form.validate()


def test_does_not_validate_too_short_username(form_data_factory) -> None:
    """
    Make sure that the form does not allow a username shorter than 4 characters

    :param form_data_factory: A factory for form data dictionaries
    """
    form_data = form_data_factory(
        {
            "username": "abc",
            "email": "email@email.com",
            "password": "Password_123",
            "password_confirmation": "Password_123",
        }
    )
    form = RegisterForm(formdata=form_data)

    assert not form.validate()


def test_does_not_validate_too_long_username(form_data_factory) -> None:
    """
    Make sure that the form does not allow a username longer than 64 characters

    :param form_data_factory: A factory for form data dictionaries
    """
    form_data = form_data_factory(
        {
            "username": "a" * 65,
            "email": "email@email.com",
            "password": "Password_123",
            "password_confirmation": "Password_123",
        }
    )
    form = RegisterForm(formdata=form_data)

    assert not form.validate()


def test_does_not_validate_invalid_email(form_data_factory) -> None:
    """
    Make sure that the form does not allow an invalid email

    :param form_data_factory: A factory for form data dictionaries
    """
    form_data = form_data_factory(
        {
            "username": "username",
            "email": "email.email.com",
            "password": "Password_123",
            "password_confirmation": "Password_123",
        }
    )
    form = RegisterForm(formdata=form_data)

    assert not form.validate()


def test_does_not_validate_too_short_password(
    form_data_factory,
) -> None:
    """
    Make sure that the form does not allow a password with less than 8 characters

    :param form_data_factory: A factory for form data dictionaries
    """
    form_data = form_data_factory(
        {
            "username": "username",
            "email": "email.email.com",
            "password": "passwor",
            "password_confirmation": "passwor",
        }
    )
    form = RegisterForm(formdata=form_data)

    assert not form.validate()


def test_does_not_validate_too_long_password(
    form_data_factory,
) -> None:
    """
    Make sure that the form does not allow a password with more than 64 characters

    :param form_data_factory: A factory for form data dictionaries
    """
    form_data = form_data_factory(
        {
            "username": "username",
            "email": "email.email.com",
            "password": "p" * 65,
            "password_confirmation": "p" * 65,
        }
    )
    form = RegisterForm(formdata=form_data)

    assert not form.validate()


def test_does_not_validate_password_with_no_lowercase_character(
    form_data_factory,
) -> None:
    """
    Make sure that the form does not allow a password without a lowercase letter

    :param form_data_factory: A factory for form data dictionaries
    """
    form_data = form_data_factory(
        {
            "username": "username",
            "email": "email.email.com",
            "password": "PASSWORD_123",
            "password_confirmation": "PASSWORD_123",
        }
    )
    form = RegisterForm(formdata=form_data)

    assert not form.validate()


def test_does_not_validate_password_with_no_uppercase_character(
    form_data_factory,
) -> None:
    """
    Make sure that the form does not allow a password without an uppercase letter

    :param form_data_factory: A factory for form data dictionaries
    """
    form_data = form_data_factory(
        {
            "username": "username",
            "email": "email.email.com",
            "password": "password_123",
            "password_confirmation": "password_123",
        }
    )
    form = RegisterForm(formdata=form_data)

    assert not form.validate()


def test_does_not_validate_password_without_digit(
    form_data_factory,
) -> None:
    """
    Make sure that the form does not allow a password without a digit

    :param form_data_factory: A factory for form data dictionaries
    """
    form_data = form_data_factory(
        {
            "username": "username",
            "email": "email.email.com",
            "password": "password_",
            "password_confirmation": "password_",
        }
    )
    form = RegisterForm(formdata=form_data)

    assert not form.validate()


def test_does_not_validate_password_with_no_special_character(
    form_data_factory,
) -> None:
    """
    Make sure that the form does not allow a password without a special character

    :param form_data_factory: A factory for form data dictionaries
    """
    form_data = form_data_factory(
        {
            "username": "username",
            "email": "email.email.com",
            "password": "password123",
            "password_confirmation": "password123",
        }
    )
    form = RegisterForm(formdata=form_data)

    assert not form.validate()


def test_does_not_validate_password_confirmation_that_doesnt_match_password(
    form_data_factory,
) -> None:
    """
    Make sure that the form does not allow a password confirmation different from the password

    :param form_data_factory: A factory for form data dictionaries
    """
    form_data = form_data_factory(
        {
            "username": "username",
            "email": "email.email.com",
            "password": "Password_123",
            "password_confirmation": "Password_1234",
        }
    )
    form = RegisterForm(formdata=form_data)

    assert not form.validate()
