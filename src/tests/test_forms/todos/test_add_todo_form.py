from uuid import uuid4
from forms.todos import AddTodoForm
from tests.utils import form_data


def test_validates_proper_input() -> None:
    """
    Make sure that the form allows proper input
    """
    category_uuid = uuid4()
    data = form_data(
        {"title": "Go to school", "date": "2024-04-17", "category": category_uuid}
    )
    form = AddTodoForm(formdata=data)
    form.category.choices = [(category_uuid, "School")]

    assert form.validate()


def test_validates_no_category() -> None:
    """
    Make sure that the form allows a record without a category
    """
    data = form_data({"title": "Go to school", "date": "2024-04-17", "category": ""})
    form = AddTodoForm(formdata=data)
    form.category.choices = [("", None)]

    assert form.validate()


def test_does_not_validate_invalid_date():
    """
    Make sure that the form not validate an invalid date
    """
    data = form_data({"title": "Go to school", "date": "2024-04-32", "category": ""})
    form = AddTodoForm(formdata=data)
    form.category.choices = [("", None)]

    assert not form.validate()
