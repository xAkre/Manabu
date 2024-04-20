from uuid import uuid4
from forms.todos import EditTodoForm
from tests.utils import form_data


def test_validates_proper_input() -> None:
    """
    Make sure that the form allows proper input
    """
    category_uuid = uuid4()
    data = form_data(
        {"title": "Go To Work", "date": "2024-12-30", "category": category_uuid}
    )
    form = EditTodoForm(formdata=data)
    form.category.choices = [(category_uuid, "School")]

    assert form.validate()
