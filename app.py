# ==============================================================================
# LOAN PREDICTION SYSTEM - FLASK WEB APPLICATION
# This is the backend that handles form submissions and makes predictions
# ==============================================================================

# Step 1: Import necessary libraries
from flask import Flask, render_template, request, jsonify  # Flask for web app
import pickle  # For loading the saved model
from sklearn.preprocessing import LabelEncoder  # For encoding data
import numpy as np  # For numerical operations

# Step 2: Initialize Flask application
app = Flask(__name__)

# Step 3: Global variables to store model and encoders
model = None
encoders = None
le_target = None

# Step 4: Load the trained model and encoders on startup
def load_model_and_encoders():
    """
    This function runs when the app starts.
    It loads the saved model and encoders from pickle files.
    """
    global model, encoders, le_target
    
    try:
        print("Loading model...")
        with open('model.pkl', 'rb') as f:
            model = pickle.load(f)
        print("✓ Model loaded successfully!")
        
        print("Loading encoders...")
        with open('encoders.pkl', 'rb') as f:
            encoders = pickle.load(f)
        print("✓ Encoders loaded successfully!")
        
        print("Loading target encoder...")
        with open('le_target.pkl', 'rb') as f:
            le_target = pickle.load(f)
        print("✓ Target encoder loaded successfully!\n")
        
    except FileNotFoundError as e:
        print(f"✗ Error: {e}")
        print("Please run train_model.py first to create the model!")
        exit()

# Step 5: Define home route (shows the form)
@app.route('/')
def home():
    """
    When user visits localhost:5000, this function runs.
    It displays the HTML form (index.html).
    """
    return render_template('index.html')

# Step 6: Define prediction route (handles form submission)
@app.route('/predict', methods=['POST'])
def predict():
    """
    When user submits the form, this function receives the data,
    preprocesses it, and makes a prediction.
    
    Expected data format (JSON):
    {
        "gender": "Male",
        "married": "Yes",
        "dependents": "2",
        "education": "Graduate",
        "self_employed": "No",
        "applicant_income": 5000,
        "loan_amount": 1500,
        "credit_history": "1"
    }
    """
    
    try:
        # Get data from the form submitted by JavaScript
        data = request.get_json()
        
        # Validate that data was received
        if data is None:
            return jsonify({
                'success': False,
                'error': 'No data received. Please check your form submission.'
            }), 400
        
        # Step 6a: Extract form inputs with validation
        gender = data.get('gender')
        married = data.get('married')
        dependents = data.get('dependents')
        education = data.get('education')
        self_employed = data.get('self_employed')
        applicant_income = data.get('applicant_income')
        loan_amount = data.get('loan_amount')
        credit_history = data.get('credit_history')
        
        # Validate all fields are present
        required_fields = ['gender', 'married', 'dependents', 'education', 'self_employed', 
                          'applicant_income', 'loan_amount', 'credit_history']
        missing_fields = [field for field in required_fields if data.get(field) is None]
        
        if missing_fields:
            return jsonify({
                'success': False,
                'error': f'Missing fields: {", ".join(missing_fields)}'
            }), 400
        
        # Convert to appropriate types
        try:
            dependents = int(dependents)
            applicant_income = int(applicant_income)
            loan_amount = int(loan_amount)
            credit_history = int(credit_history)
        except (ValueError, TypeError) as e:
            return jsonify({
                'success': False,
                'error': f'Invalid data types: {str(e)}'
            }), 400
        
        # Step 6b: Encode categorical variables using saved encoders
        # Convert text values to numbers using the encoders trained on training data
        try:
            gender_encoded = encoders['Gender'].transform([gender])[0]
            married_encoded = encoders['Married'].transform([married])[0]
            education_encoded = encoders['Education'].transform([education])[0]
            self_employed_encoded = encoders['Self_Employed'].transform([self_employed])[0]
        except (KeyError, ValueError) as e:
            return jsonify({
                'success': False,
                'error': f'Invalid category value: {str(e)}'
            }), 400
        
        # Step 6c: Prepare the feature array for prediction
        # This should be in the same order as training data
        features = np.array([[
            gender_encoded,           # 0: Gender
            married_encoded,          # 1: Married
            dependents,               # 2: Dependents
            education_encoded,        # 3: Education
            self_employed_encoded,    # 4: Self_Employed
            applicant_income,         # 5: Applicant_Income
            loan_amount,              # 6: Loan_Amount
            credit_history            # 7: Credit_History
        ]])
        
        # Step 6d: Make prediction using the trained model
        try:
            prediction = model.predict(features)[0]  # Get prediction (0 or 1)
            probability = model.predict_proba(features)[0]  # Get probability scores
            
            # Step 6e: Decode the prediction back to original labels
            prediction_label = le_target.inverse_transform([prediction])[0]
            
            # Get confidence score (probability of the predicted class)
            confidence = max(probability) * 100
        except Exception as pred_error:
            return jsonify({
                'success': False,
                'error': f'Prediction error: {str(pred_error)}'
            }), 500
        
        # Create response
        response = {
            'success': True,
            'prediction': prediction_label,  # 'Y' or 'N'
            'confidence': f"{confidence:.2f}%",
            'approved': prediction_label == 'Y'  # True if approved, False if rejected
        }
        
        return jsonify(response)
    
    except Exception as e:
        # If there's an error, return error message
        return jsonify({
            'success': False,
            'error': str(e)
        }), 400

# Step 7: Run the Flask application
if __name__ == '__main__':
    # Load model and encoders before starting the app
    load_model_and_encoders()
    
    print("=" * 60)
    print("LOAN PREDICTION SYSTEM - FLASK SERVER")
    print("=" * 60)
    print("\n✓ Server starting...")
    print("✓ Open your browser and go to: http://localhost:5000")
    print("✓ Press Ctrl+C to stop the server\n")
    
    # Start the Flask development server
    # debug=True means the server will reload when you make changes
    # host='0.0.0.0' makes it accessible from any address
    app.run(debug=True, host='0.0.0.0', port=8000)
