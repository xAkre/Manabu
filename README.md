# Manabu

## Description

Manabu is a full-stack todo application designed to help users organize their tasks efficiently. Users can create,
manage, and categorize their todos conveniently through a user-friendly interface.

## Features

- **User Authentication**: Users can sign up and log in securely to access their todos.
- **Todo Creation**: Users can create new todos with titles, descriptions, due dates, and categories.
- **Todo Management**: Users can view, edit, mark as complete, and delete their todos.
- **Category Management**: Users can categorize their todos into different categories for better organization.
- **Database Integration**: Todos are stored in a database to ensure data persistence and accessibility across sessions.
- **Responsive Design**: The application is designed to work seamlessly across various devices and screen sizes.

## Running the app locally

1. Clone the repository.
2. Download and install [Python](https://www.python.org/downloads/).
3. Run `pip install .` to install Python dependencies.
4. Download and install [Node.js](https://nodejs.org/en).
5. Run `npm install` to install Node.js dependencies.
6. Run `npm run tailwind-build` to build TailwindCSS styles.
7. Run `flask --app src/index.py run` to start the Flask server.
8. The app should be running on [http://127.0.0.1:5000](http://127.0.0.1:5000).

## Technologies used

- [Python](https://www.python.org/): Backend language
- [Flask](https://flask.palletsprojects.com/en/3.0.x/): Backend framework
- [SQLAlchemy](https://www.sqlalchemy.org/): Database ORM
- [Pytest](https://www.pytest.org/): Testing framework
- [TailwindCSS](https://tailwindcss.com/): CSS Framework
- [Jinja](https://jinja.palletsprojects.com/en/3.1.x/): Templating engine

## Testing

To run tests:

1. Navigate to the project directory.
2. Run `pip install .[test]` to install test dependencies.
3. Run `pytest` to execute the test suite.