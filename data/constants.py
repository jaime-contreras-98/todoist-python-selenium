import os
from dotenv import load_dotenv
from faker import Faker


class Constants(object):
    load_dotenv()
    data = Faker()

    url = [
        "https://todoist.com/es",
        "UAT",
        "DEV",
        "TEST"
    ]

    dates = [
        "Today",
        "Tomorrow",
        "Weekend",
        "Next Week"
    ]

    error_msg = [
        "Email o contraseña incorrectos.",
        "Las contraseñas deben tener al menos 8 caracteres.",
        "Introduce una dirección de email válida."
    ]

    tasks_data = [
        "Name: " + data.uuid4(),
        "Description: " + data.uuid4()
    ]

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
