# ==============================================================================
# LOAN PREDICTION SYSTEM - MODEL TRAINING SCRIPT
# This script prepares the data and trains a machine learning model
# ==============================================================================

# Step 1: Import necessary libraries
import pandas as pd  # For data handling
import numpy as np   # For numerical operations
from sklearn.preprocessing import LabelEncoder  # For converting text to numbers
from sklearn.linear_model import LogisticRegression  # ML model for classification
from sklearn.model_selection import train_test_split  # To split data into train and test
import pickle  # For saving the trained model

print("=" * 60)
print("LOAN PREDICTION SYSTEM - MODEL TRAINING")
print("=" * 60)

# Step 2: Load the dataset
print("\n1. Loading dataset from loan_data.csv...")
try:
    df = pd.read_csv('loan_data.csv')
    print(f"   ✓ Dataset loaded successfully!")
    print(f"   → Total records: {len(df)}")
    print(f"   → Total features: {len(df.columns)}\n")
except FileNotFoundError:
    print("   ✗ Error: loan_data.csv not found!")
    exit()

# Step 3: Display basic information about the dataset
print("2. Dataset Overview:")
print(f"   Shape: {df.shape}")
print(f"   Columns: {list(df.columns)}\n")

# Step 4: Handle missing values (if any)
print("3. Checking for missing values...")
missing_values = df.isnull().sum()
if missing_values.sum() == 0:
    print("   ✓ No missing values found!\n")
else:
    print(f"   Missing values:\n{missing_values}\n")
    # Fill missing values if needed
    df = df.fillna(df.mean(numeric_only=True))

# Step 5: Separate features (X) and target (y)
print("4. Preparing data for training...")
# Features (what we use to predict) - drop the target variable
X = df.drop('Loan_Status', axis=1)
# Target (what we want to predict)
y = df['Loan_Status']
print(f"   Features (X): {list(X.columns)}")
print(f"   Target (y): Loan_Status\n")

# Step 6: Encode categorical variables (convert text to numbers)
print("5. Encoding categorical variables...")
# Dictionary to store encoders (for later use in Flask app)
encoders = {}

# List of categorical columns
categorical_cols = ['Gender', 'Married', 'Education', 'Self_Employed']

for col in categorical_cols:
    le = LabelEncoder()  # Create encoder
    X[col] = le.fit_transform(X[col])  # Convert categories to numbers
    encoders[col] = le  # Save encoder for later use
    print(f"   ✓ {col} encoded: {dict(zip(le.classes_, le.transform(le.classes_)))}")

# Encode target variable
le_target = LabelEncoder()
y = le_target.fit_transform(y)
print(f"   ✓ Loan_Status encoded: {dict(zip(le_target.classes_, le_target.transform(le_target.classes_)))}\n")

# Step 7: Split data into training and testing sets
print("6. Splitting data into training and testing sets...")
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)
print(f"   Training samples: {len(X_train)}")
print(f"   Testing samples: {len(X_test)}\n")

# Step 8: Train the Logistic Regression model
print("7. Training Logistic Regression model...")
model = LogisticRegression(random_state=42, max_iter=1000)
model.fit(X_train, y_train)
print("   ✓ Model training completed!\n")

# Step 9: Evaluate model performance
print("8. Model Evaluation:")
train_score = model.score(X_train, y_train)
test_score = model.score(X_test, y_test)
print(f"   Training Accuracy: {train_score:.2%}")
print(f"   Testing Accuracy: {test_score:.2%}\n")

# Step 10: Save the model and encoders
print("9. Saving model and encoders...")
# Save model
with open('model.pkl', 'wb') as f:
    pickle.dump(model, f)
print("   ✓ Model saved as 'model.pkl'")

# Save encoders
with open('encoders.pkl', 'wb') as f:
    pickle.dump(encoders, f)
print("   ✓ Encoders saved as 'encoders.pkl'")

# Save label encoder for target variable
with open('le_target.pkl', 'wb') as f:
    pickle.dump(le_target, f)
print("   ✓ Target encoder saved as 'le_target.pkl'\n")

print("=" * 60)
print("MODEL TRAINING COMPLETED SUCCESSFULLY!")
print("=" * 60)
print("\nYou can now run the Flask app with: python app.py")
