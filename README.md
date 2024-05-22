# README

## Title

Experience Points Converter (XPC)

## Description

This is a server microservice that converts time spent on an activity into the appropriate earned amount of experience points (XP). A client program can call the Experience Points Converter and pass the amount of time to be converted in minutes, and receive the correct amount of experience points in response.

## Installation

The XPC requires the following dependencies:
    
- Python 3.x
- Flask 3.0.x

Python 3.x can be installed by visiting:

```
https://www.python.org/downloads/
```
    
Flask is installed at the command prompt with Windows or terminal with macOS/Linux with the following prompt:

Flask:

```
pip3 install Flask
```

The XPC can be downloaded from this GitHub repository, the file name is:

```
xp-converter.py
```

## Client Program Setup (Requesting Data)

The XPC receives data via an http POST request in the form of a JSON object. The JSON object must use the key "time_in_minutes" and the value must be a floating point number or an integer. Example:

```
{"time_in_minutes": 40}
```

The XPC is run on a local host, and the default port is 5000. This can be changed by editing the PORT constant in the xp-converter.py file. The default url for the client to send a request to is:

```
http://127.0.0.1:5000/
```

If you have modified the port to be something other than 5000, you need to change the 5000 portion of the url in the client to match the port you have chosen.

A sample client program time-client.py has been provided in this GitHub repository to help demonstrate how to interact with the XPC.

## Running the Microservice (Receiving Data)

1. Install the required dependencies.
2. While in the local directory where xp-converter.py is located on your computer, using the command prompt (Windows) or terminal (macOS/Linux) use the following prompt to run the server:

```
python3 xp-converter.py
```

3. Make a request to the XPC server. Here is an example call from the sample client program time-client.py (the requests Python library would need to be installed previously using the "pip3 install requests" prompt):

```
import requests
import json

url = "http://127.0.0.1:5000/"
data = {"time_in_minutes": 40}  # Sample data
json_data = json.dumps(data)
headers = {"Content-Type": "application/json"}
response = requests.post(url, data=json_data, headers=headers)
print(response.json())
```  

4. The XPC will automatically respond to the client with a JSON object in the following format (the xp variable value is the experience points gained in a floating point number data type):

```
{"xp_gained": xp}
```
