import requests
import json

URL = "http://127.0.0.1:8000/student_drf/student_api/"

def delete_data():
    data = { 'id': 2  }
    json_data = json.dumps(data)
    r = requests.delete(url = URL, data = json_data) # Here, we are sending the data to the server.
    python_data = r.json() # Converts the JSON data into a Python dictionary.
    print(python_data) # Output: {'msg': 'Data deleted successfully'}

delete_data()