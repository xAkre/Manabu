from forms.categories import EditCategoryForm
from tests.utils import form_data


def test_validates_proper_input():
    """
    Make sure that the form allows proper input
    """
    data = form_data({"name": "School", "color": "#FFFFFF"})
    form = EditCategoryForm(formdata=data)

    assert form.validate()
