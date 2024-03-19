from wtforms import Form, StringField, ColorField, validators


class AddCategoryForm(Form):
    """
    Represents a form that adds a category
    """

    name = StringField(
        label="Name",
        name="name",
        validators=[
            validators.input_required(message="Name is required"),
            validators.length(
                min=4, max=64, message="Category name must 4 - 64 characters"
            ),
        ],
    )

    # <input type="color"> should not be used on the frontend, and this field is only here for validation
    # server side. Use coloris on the frontend
    color = ColorField(
        label="Color",
        name="color",
        validators=[
            validators.input_required(message="Color is required"),
            validators.regexp(
                regex="^#([A-Fa-f0-9]{6}|[A-Fa-f0-9]{3})$",
                message="Color must be a valid hex color",
            ),
        ],
    )
