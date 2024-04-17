from wtforms import Form, StringField, DateField, validators, SelectField


class AddTodoForm(Form):
    """
    Represents a form that adds a todo
    """

    title = StringField(
        label="Title",
        name="title",
        validators=[
            validators.input_required(message="Title is required"),
            validators.length(
                min=4, max=64, message="Todo title must 4 - 128 characters"
            ),
        ],
    )

    date = DateField(
        label="Date",
        name="date",
        validators=[
            validators.input_required(message="Date is required"),
        ],
    )

    category = SelectField(label="Category", name="category")
