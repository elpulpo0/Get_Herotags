from flask import Flask, jsonify, request
from pymongo import MongoClient
from flask_cors import CORS
import os
from dotenv import load_dotenv

# Initialize Flask app
app = Flask(__name__)

# Configure CORS to allow multiple origins
CORS(app, resources={r"/get_herotags": {"origins": ["http://localhost:5173", "https://pfp.kwak.lol"]}})

# Load environment variables
load_dotenv()
MONGO_URI = os.getenv("MONGO_URI")

# Connect to MongoDB
try:
    client = MongoClient(MONGO_URI)
    db = client['herotag']
    collection = db['herotag_list']
    print("Connected to MongoDB")
except Exception as e:
    print(f"Error connecting to MongoDB: {e}")
    exit()

@app.route("/get_herotags", methods=["GET", "POST"])
def get_herotags():
    if request.method == "GET":
        # Get addresses from URL parameters
        addresses = request.args.get("addresses")
        if addresses:
            addresses = addresses.split(",")  # Split the string into a list
        else:
            return jsonify({"error": "No addresses provided in the URL."}), 400

        # MongoDB query to find herotags by address
        query = {"address": {"$in": addresses}}
        results = collection.find(query, {"address": 1, "userName": 1})

        # Create response with address and herotag
        response_data = [{"address": result["address"], "herotag": result["userName"]} for result in results]

        return jsonify(response_data)

    elif request.method == "POST":
        data = request.get_json()
        addresses = data.get("addresses", [])

        if not addresses:
            return jsonify({"error": "The list of addresses is empty or missing."}), 400

        # MongoDB query to find herotags by address
        query = {"address": {"$in": addresses}}
        results = collection.find(query, {"address": 1, "userName": 1})

        # Create response with address and herotag
        response_data = [{"address": result["address"], "herotag": result["userName"]} for result in results]

        return jsonify(response_data)

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=False)
