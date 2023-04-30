from flask import Flask, send_from_directory, request, jsonify
from flask_pymongo import PyMongo
import os

app = Flask(__name__, static_folder="static")

# Configure the connection to the MongoDB database
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
mongo = PyMongo(app)

@app.route("/")
def index():
    return send_from_directory(app.static_folder, "index.html")

# API endpoint to save the email
@app.route('/join', methods=['POST'])
def save_email():
    email = request.form.get('email')
    mongo.db.emails.insert_one({"email": email})
    return jsonify({"result": "Email saved"}), 201

# API endpoint to save the feedback
@app.route('/feedback', methods=['POST'])
def save_feedback():
    feedback = request.form.get('feedback')
    mongo.db.feedbacks.insert_one({"feedback": feedback})
    return jsonify({"result": "Feedback saved"}), 201

if __name__ == '__main__':
    app.run(debug=True)
