from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from werkzeug.utils import secure_filename
import os
from endpoints.fraud_detection import predict_fraud  # Importing fraud prediction function
from endpoints.forgery_detection import detect_forgery  # Import forgery detection function
from utils.preprocess import preprocess  # Importing preprocess function from utils.preprocess.py

app = Flask(__name__)

# Configure the database URI (replace with your actual database credentials)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://ritika:Payal%401234@localhost/fraud_detection_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Configure upload folder
UPLOAD_FOLDER = 'uploads/'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Initialize the database and migration
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Define a table model for storing predictions
class FraudPrediction(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    policy_number = db.Column(db.String(50), nullable=False)
    fraud_category = db.Column(db.String(100), nullable=False)
    probability = db.Column(db.Float, nullable=False)
    fraud_score = db.Column(db.Float, nullable=False)  # New field to store the fraud score

# Define a table model for storing forgery detections
class ForgeryDetection(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    policy_id = db.Column(db.String(50), nullable=False)
    forgery_score = db.Column(db.Float, nullable=False)
    status = db.Column(db.String(50), nullable=False)  # Example: "Forgery Detected" or "Clean"

# Root route
@app.route('/')
def home():
    return jsonify({"message": "Welcome to the Flask app!"})

@app.route('/detect_fraud', methods=['POST'])
def detect_fraud():
    try:
        # Parse input data
        data = request.json
        if not data or 'policy_number' not in data or 'features' not in data:
            return jsonify({"error": "Invalid input format. Provide 'policy_number' and 'features'."}), 400

        policy_number = data['policy_number']
        features = data['features']

        # Check if features have 23 values
        if len(features) != 23:
            return jsonify({"error": "Features list should contain 23 values."}), 400

        # Preprocess the input features using the preprocess function
        processed_features = preprocess(features)
        print(f"Processed features: {processed_features}")

        # Call fraud detection function
        fraud_category, probability, fraud_score = predict_fraud(processed_features)

        if fraud_category is None or probability is None or fraud_score is None:
            return jsonify({"error": "Failed to detect fraud. Ensure the input is valid and the model is functioning correctly."}), 500

        # Save to database
        prediction = FraudPrediction(
            policy_number=policy_number,
            fraud_category=fraud_category,
            probability=probability,
            fraud_score=fraud_score
        )
        db.session.add(prediction)
        db.session.commit()

        # Return the result as a JSON response
        return jsonify({
            "policy_number": policy_number,
            "fraud_category": fraud_category,
            "probability": probability,
            "fraud_score": fraud_score,
            "message": "Fraud detection completed and result saved to database."
        }), 200

    except Exception as e:
        print(f"Error in detect_fraud endpoint: {e}")
        return jsonify({"error": str(e)}), 500

# Detect forgery and save to database
@app.route('/detect_forgery', methods=['POST'])
def detect_forgery_route():
    try:
        # Check if 'policy_id' and 'image' are in the request
        if 'policy_id' not in request.form or 'image' not in request.files:
            return jsonify({"error": "Invalid input format. Provide 'policy_id' and an image file."}), 400

        policy_id = request.form['policy_id']
        image = request.files['image']

        # Save the uploaded image
        filename = secure_filename(image.filename)
        image_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        image.save(image_path)


        forgery_result = detect_forgery(image_path)  # Get the result from detect_forgery function

        forgery_score = float(forgery_result['forgery_score'])  # Get the actual forgery score
        status = forgery_result['status']  # Get the forgery status
        
        
        # Save to database
        forgery_record = ForgeryDetection(
            policy_id=policy_id,
            forgery_score=forgery_score,
            status=status
        )
        db.session.add(forgery_record)
        db.session.commit()

        # Return the result as a JSON response
        return jsonify({
            "policy_id": policy_id,
            "forgery_score": forgery_score,
            "status": status,
            "message": "Forgery detection completed and result saved to database."
        }), 200

    except Exception as e:
        print(f"Error in detect_forgery endpoint: {e}")
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
