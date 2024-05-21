# Citation for the following Python file:
# Date: 5/20/2024
# Adapted from: Flask Documentation (3.0.x)
# Source URL: https://flask.palletsprojects.com/en/3.0.x/
# Server for the experience points converter microservice.
# Author: Christopher McLean

from flask import Flask, request, jsonify

app = Flask(__name__)

PORT = 5000
CONVERSION_RATE = 10.0


@app.route('/', methods=['POST'])
def xp_converter():
    data = request.get_json()

    if not data:
        return jsonify({"error": "Data not found, please try again."}), 400

    if "time_in_minutes" not in data:
        return jsonify({"error": "time_in_minutes not found, please try again."}), 400

    try:
        time = float(data["time_in_minutes"])
    except (ValueError, TypeError):
        return jsonify({"error": "incorrect data type for time_in_minutes, please try again."}), 400

    xp = time * CONVERSION_RATE
    return jsonify({"xp_gained": xp}), 200


if __name__ == "__main__":
    app.run(port=PORT)
