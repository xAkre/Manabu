from forms.categories import AddCategoryForm


def test_validates_proper_input(form_data_factory):
    """
    Make sure that the form allows proper input

    :param form_data_factory: A factory for form data dictionaries
    """
    form_data = form_data_factory({"name": "School", "color": "#FFFFFF"})
    form = AddCategoryForm(formdata=form_data)

    assert form.validate()


def test_does_not_validate_too_short_name(form_data_factory):
    """
    Make sure that the form does not allow a name shorter than 4 characters

    :param form_data_factory: A factory for form data dictionaries
    """
    form_data = form_data_factory({"name": "abc", "color": "#FFFFFF"})
    form = AddCategoryForm(formdata=form_data)

    assert not form.validate()


def test_does_not_validate_too_long_name(form_data_factory):
    """
    Make sure that the form does not allow a name longer than 64 characters

    :param form_data_factory: A factory for form data dictionaries
    """
    form_data = form_data_factory({"name": "a" * 65, "color": "#FFFFFF"})
    form = AddCategoryForm(formdata=form_data)

    assert not form.validate()


def test_does_not_validate_invalid_hex_color(form_data_factory):
    """
    Make sure that the form does not allow an invalid hex

    :param form_data_factory: A factory for form data dictionaries
    """
    form_data = form_data_factory({"name": "School", "color": "#FFFFF"})
    form = AddCategoryForm(formdata=form_data)

    assert not form.validate()
