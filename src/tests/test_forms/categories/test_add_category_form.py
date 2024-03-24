from forms.categories import AddCategoryForm
from tests.utils import form_data


def test_validates_proper_input():
    """
    Make sure that the form allows proper input
    """
    data = form_data({"name": "School", "color": "#FFFFFF"})
    form = AddCategoryForm(formdata=data)

    assert form.validate()


def test_does_not_validate_too_short_name():
    """
    Make sure that the form does not allow a name shorter than 4 characters
    """
    data = form_data({"name": "abc", "color": "#FFFFFF"})
    form = AddCategoryForm(formdata=data)

    assert not form.validate()


def test_does_not_validate_too_long_name():
    """
    Make sure that the form does not allow a name longer than 64 characters
    """
    data = form_data({"name": "a" * 65, "color": "#FFFFFF"})
    form = AddCategoryForm(formdata=data)

    assert not form.validate()


def test_does_not_validate_invalid_hex_color():
    """
    Make sure that the form does not allow an invalid hex
    """
    data = form_data({"name": "School", "color": "#FFFFF"})
    form = AddCategoryForm(formdata=data)

    assert not form.validate()
