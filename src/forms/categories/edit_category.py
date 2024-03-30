from wtforms import StringField, validators
from .add_category import AddCategoryForm


class EditCategoryForm(AddCategoryForm):
    """
    Represents a form that edits a category. Contains all the fields required inside the add category form
    """
