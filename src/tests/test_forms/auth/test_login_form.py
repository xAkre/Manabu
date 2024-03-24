from forms.auth import LoginForm
from tests.utils import form_data


def test_validates_proper_input() -> None:
    """
    Make sure that the form allows proper input
    """
    data = form_data({"username_or_email": "username", "password": "Password_123"})
    form = LoginForm(formdata=data)

    assert form.validate()
