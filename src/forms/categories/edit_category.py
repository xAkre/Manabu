from wtforms import StringField, validators
from .add_category import AddCategoryForm


class EditCategoryForm(AddCategoryForm):
    """
    Represents a form that edits a category. Contains all the fields required inside the add category form
    """

    category_id = StringField(
        name="category_uuid",
        validators=[
            validators.input_required(message="Category uuid is required"),
            validators.length(
                min=36, max=36, message="Category uuid must be a valid v4 uuid"
            ),
        ],
    )
