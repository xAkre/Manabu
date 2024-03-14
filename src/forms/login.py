from wtforms import Form, StringField, EmailField, PasswordField, validators


class LoginForm(Form):
    """
    Represents a login form
    """

    username_or_email = StringField(
        label="Username or Email",
        name="username_or_email",
        validators=[validators.input_required()],
    )
    password = PasswordField(
        label="Password", name="password", validators=[validators.input_required()]
    )
