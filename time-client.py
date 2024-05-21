# Citation for the following Python file:
# Date: 5/20/2024
# Adapted from: Flask Documentation (3.0.x)
# Source URL: https://flask.palletsprojects.com/en/3.0.x/
# A test client for the experience points converter microservice.
# Author: Christopher McLean

import requests
import json

url = "http://127.0.0.1:5000/"
data = {"time_in_minutes": 40}  # Sample data
json_data = json.dumps(data)
headers = {"Content-Type": "application/json"}
response = requests.post(url, data=json_data, headers=headers)
print(response.json())
