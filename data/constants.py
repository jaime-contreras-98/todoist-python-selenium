import os
from dotenv import load_dotenv
from faker import Faker


class Constants(object):
    load_dotenv()
    data = Faker()

    url = {
        "prod": "https://todoist.com/es",
        "UAT": "dsad",
        "DEV": "dsad",
        "TEST": "dsad"
    }

    dates = {
        "today": "today",
        "tomorrow": "tomorrow",
        "week": "weekend",
        "next": "nextweek"
    }

    error_msg = {
        "bad_credentials": "Email o contraseña incorrectos.",
        "bad_password": "Las contraseñas deben tener al menos 8 caracteres.",
        "bad_email": "Introduce una dirección de email válida."
    }

    tasks_data = {
        "name": "Task Name: " + data.uuid4(),
        "description": "Task Description: " + data.uuid4()
    }

    project_data = {
        "name": "Project Name: " + data.uuid4(),
        "view": {
            "list": "list_view_",
            "panel": "list_board_"
        }
    }

    section_data = {
        "name": "Section Name: " + data.uuid4()
    }

    credentials = {
        "users": {
            "real": {
                "user": os.getenv('REAL_USERNAME'),
                "pass": os.getenv('REAL_PASSWORD')
            },
            "fake": {
                "user": os.getenv('FAKE_USERNAME'),
                "pass": os.getenv('FAKE_PASSWORD')
            }
        }
    }
