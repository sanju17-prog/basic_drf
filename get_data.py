import json
import requests

URL = "http://127.0.0.1:8000/get_student/"

def get_data(id = None):
    data = {}
    if id is not None:
        data = {'id': id}
    json_data = json.dumps(data)
    r = requests.get(url = URL, data = json_data)
    data = r.json() # Converts the JSON data into a Python dictionary.
    print(data)

get_data()