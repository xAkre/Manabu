from wtforms import Form, BooleanField


class SetCompletedStatusTodoForm(Form):
    """
    Represents a form that sets the completed status of a todo
    """

    status = BooleanField(label="Status", name="status")
