from flask import Flask, request, jsonify

app = Flask(__name__)

# Data storage (for demonstration purposes)
data_storage = []

# Route for handling GET requests
@app.route('/data', methods=['GET'])
def get_data():
    return jsonify({"data": data_storage}), 200

# Route for handling POST requests
@app.route('/data', methods=['POST'])
def post_data():
    # Retrieve JSON data from the POST request
    new_data = request.json
    if not new_data:
        return jsonify({"error": "No data provided"}), 400

    # Add the data to storage
    data_storage.append(new_data)
    return jsonify({"message": "Data added successfully", "data": new_data}), 201

if __name__ == '__main__':
    app.run(debug=True)
