from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from endpoints.fraud_detection import process_fraud_detection
from utils.preprocess import preprocess  # Assuming the preprocess function is imported from utils/preprocess.py

app = Flask(__name__)

# Configure the database URI (replace with your actual database credentials)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://mrigank:mrigank%4011@localhost/fraud_detection_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Define a table model for storing predictions
class FraudPrediction(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    policy_number = db.Column(db.String(50), nullable=False)
    fraud_category = db.Column(db.String(100), nullable=False)
    probability = db.Column(db.Float, nullable=False)

# Root route
@app.route('/')
def home():
    return jsonify({"message": "Welcome to the Flask app!"})

# Detect fraud and save to database
@app.route('/detect_fraud', methods=['POST'])
def detect_fraud():
    try:
        # Parse input data
        data = request.json
        if not data or 'policy_number' not in data or 'features' not in data:
            return jsonify({"error": "Invalid input format. Provide 'policy_number' and 'features'."}), 400

        policy_number = data['policy_number']
        features = data['features']

        # Preprocess the input features using the preprocess function
        processed_features = preprocess(features)

        # Call fraud detection function (which removes policy_number from features)
        fraud_category, probability = process_fraud_detection(processed_features)

        # Save to database
        prediction = FraudPrediction(
            policy_number=policy_number,
            fraud_category=fraud_category,
            probability=probability
        )
        db.session.add(prediction)
        db.session.commit()

        # Return the result as a JSON response
        return jsonify({
            "policy_number": policy_number,
            "fraud_category": fraud_category,
            "probability": probability,
            "message": "Fraud detection completed and result saved to database."
        }), 200
    except Exception as e:
        print(f"Error in detect_fraud endpoint: {e}")
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    # Initialize the database tables if they are not created already
    with app.app_context():
        db.create_all()

    # Start the Flask application
    app.run(debug=True)
