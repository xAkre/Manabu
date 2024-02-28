# Manabu

## Description

Manabu is a simple todo app that allows you to add, edit, and delete tasks. It also allows you to mark tasks as
complete.

## Running the app locally

1. Clone the repository
2. Download and install [Python](https://www.python.org/downloads/)
3. Run `pip install -r requirements.txt`
4. Run `flask --app src/index.py run`
5. The app should be running on `http://127.0.0.1:5000`

## Technologies Used

- [Python](https://www.python.org/) Backend language
- [Flask](https://flask.palletsprojects.com/en/3.0.x/) Backend framework
- [SQLAlchemy](https://www.sqlalchemy.org/) Database ORM
- [Pytest](https://www.pytest.org/) Testing framework

## Currently Working On

- Creating SQLAlchemy database models
- Scoping database sessions properly. This means that a new database session should be created on every request,
similar to Flask's session
- Creating some basic helper functions for common functionality
- Creating tests
