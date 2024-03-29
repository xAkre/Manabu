from uuid import uuid4
from forms.categories import EditCategoryForm
from tests.utils import form_data


def test_validates_proper_input():
    """
    Make sure that the form allows proper input
    """
    data = form_data(
        {"name": "School", "color": "#FFFFFF", "category_uuid": str(uuid4())}
    )
    form = EditCategoryForm(formdata=data)

    assert form.validate()


def test_does_not_validate_lack_of_category_uuid():
    """
    Make sure that the form does not validate a form without a category uuid
    """
    data = form_data({"name": "School", "color": "#FFFFFF"})
    form = EditCategoryForm(formdata=data)

    assert not form.validate()


def test_does_not_validate_invalid_category_uuid():
    """
    Make sure that the form does not validate a form with an invalid uuid
    """
    data = form_data({"name": "School", "color": "#FFFFFF", "category_id": "in-va-lid-uuid"})
    form = EditCategoryForm(formdata=data)

    assert not form.validate()
