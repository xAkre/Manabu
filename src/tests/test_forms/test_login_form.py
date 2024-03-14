from forms import LoginForm


def test_validates_proper_input(form_data_factory) -> None:
    """
    Make sure that the form allows proper input

    :param form_data_factory: A factory for form data dictionaries
    """
    form_data = form_data_factory(
        {"username_or_email": "username", "password": "Password_123"}
    )
    form = LoginForm(formdata=form_data)

    assert form.validate()
