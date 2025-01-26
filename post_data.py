import requests
import json

URL = "http://127.0.0.1:8000/create_student/"

def post_data():
    data = {
        'name': 'Veena',
        'age': 23,
        'roll': 80,
        'city': 'Chennai'
    }

    json_data = json.dumps(data)
    r = requests.post(url = URL, data = json_data) # Here, we are sending the data to the server.
    python_data = r.json() # Converts the JSON data into a Python dictionary.
    print(python_data)

post_data()