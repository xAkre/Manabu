from wtforms import BooleanField, validators
from .add_todo import AddTodoForm


class EditTodoForm(AddTodoForm):
    """
    Represents a form that edits a todo. Contains all the fields required inside the add todo form
    """

    completed = BooleanField(label="Completed", name="completed")
