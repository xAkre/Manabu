from wtforms import Form, StringField, EmailField, PasswordField, validators


class RegisterForm(Form):
    """
    Represents a registration form
    """

    username = StringField(
        label="Username",
        name="username",
        validators=[
            validators.input_required(message="Username is required"),
            validators.length(
                min=4, max=64, message="Username must be 4 - 64 characters long"
            ),
        ],
    )
    email = EmailField(
        label="Email",
        name="email",
        validators=[
            validators.input_required(message="Email is required"),
            validators.email(message="Invalid email"),
        ],
    )
    password = PasswordField(
        label="Password",
        name="password",
        validators=[
            validators.input_required(message="Password is required"),
            validators.length(
                min=8, max=64, message="Password must be 8 - 64 characters long"
            ),
            validators.regexp(
                regex=r".*[a-z].*",
                message="Password must contain at least one lowercase letter",
            ),
            validators.regexp(
                regex=r".*[A-Z].*",
                message="Password must contain at least one uppercase letter",
            ),
            validators.regexp(
                regex=r".*[0-9].*", message="Password must contain at least one digit"
            ),
            validators.regexp(
                regex=r".*[\-_!@:;\=#\$%\^&\*\(\)\?].*",
                message='Password must contain at least one special character from the following: "-_!@:;=#$%^&*()"',
            ),
        ],
    )
    password_confirmation = PasswordField(
        label="Password Confirmation",
        name="password_confirmation",
        validators=[
            validators.input_required(message="Password confirmation is required"),
            validators.equal_to(
                fieldname="password",
                message="Password confirmation must match the password",
            ),
        ],
    )
