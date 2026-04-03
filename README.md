# 🏦 Loan Prediction System

A beginner-friendly web application that predicts loan approval using Machine Learning.

## 📋 Project Overview

This project demonstrates:

- **Frontend**: HTML, CSS, JavaScript for user interface
- **Backend**: Python Flask for handling requests
- **Machine Learning**: scikit-learn for loan prediction
- **Data Science**: Python pandas for data processing

Perfect for 2nd-year college projects and learning purposes!

---

## 📁 Project Structure

```
loan-prediction-system/
│
├── app.py                 # Flask backend application
├── train_model.py         # Script to train ML model
├── loan_data.csv          # Sample dataset
├── model.pkl              # Trained model (generated after running train_model.py)
├── encoders.pkl           # Categorical encoders (generated)
├── le_target.pkl          # Target encoder (generated)
├── templates/
│   └── index.html         # Frontend HTML form
├── static/
│   └── style.css          # CSS styling
└── README.md              # This file
```

---

## ⚙️ Installation & Setup

### Step 1: Install Python (if not already installed)

- Download from [python.org](https://www.python.org)
- Make sure Python 3.8+ is installed

### Step 2: Create Project Folder (if not done)

```bash
mkdir loan-prediction-system
cd loan-prediction-system
```

### Step 3: Create Virtual Environment (Recommended)

**On macOS/Linux:**

```bash
python3 -m venv env
source env/bin/activate
```

**On Windows:**

```bash
python -m venv env
env\Scripts\activate
```

### Step 4: Install Required Libraries

```bash
pip install flask pandas scikit-learn numpy
```

**What each library does:**

- `flask` - Creates the web server
- `pandas` - Handles CSV data
- `scikit-learn` - Machine Learning algorithms
- `numpy` - Numerical operations

---

## 🤖 Step-by-Step Usage

### Step 1: Train the Model

Run this command to create and train the ML model:

```bash
python train_model.py
```

**Expected Output:**

```
============================================================
LOAN PREDICTION SYSTEM - MODEL TRAINING
============================================================

1. Loading dataset from loan_data.csv...
   ✓ Dataset loaded successfully!
   → Total records: 30
   → Total features: 9

2. Dataset Overview:
   Shape: (30, 9)
   ...

9. Saving model and encoders...
   ✓ Model saved as 'model.pkl'
   ✓ Encoders saved as 'encoders.pkl'
   ✓ Target encoder saved as 'le_target.pkl'

============================================================
MODEL TRAINING COMPLETED SUCCESSFULLY!
============================================================
```

**What this step does:**

1. Loads the loan data from `loan_data.csv`
2. Handles missing values
3. Converts text to numbers (encoding)
4. Trains the Logistic Regression model
5. Saves the model as `model.pkl`

### Step 2: Run the Flask Application

```bash
python app.py
```

**Expected Output:**

```
============================================================
LOAN PREDICTION SYSTEM - FLASK SERVER
============================================================

✓ Server starting...
✓ Open your browser and go to: http://localhost:5000
✓ Press Ctrl+C to stop the server

 * Running on http://0.0.0.0:5000
```

### Step 3: Open in Web Browser

1. Open your web browser (Chrome, Firefox, Safari, etc.)
2. Go to: **`http://localhost:5000`**
3. Fill the form with applicant details
4. Click "Predict Loan Status"
5. See the result! ✓

### Step 4: Stop the Server

Press **`Ctrl+C`** in the terminal where the Flask app is running.

---

## 📊 Input Features Explained

**Gender**: Male or Female - Affects approval probability

**Married**: Yes or No - Marital status of applicant

**Dependents**: Number of dependents (0-4+) - Affects income requirement

**Education**: Graduate or Not Graduate - Education level

**Self Employed**: Yes or No - Employment status

**Applicant Income**: Monthly/Annual income in rupees (₹) - Higher income = Better approval chance

**Loan Amount**: Requested loan amount in rupees (₹) - Large loans are riskier

**Credit History**: Yes (1) or No (0) - Credit record importance (1 = has good history)

---

## 🔍 How the ML Model Works

### Training Process:

1. **Load Data** → Read loan_data.csv
2. **Clean Data** → Handle missing values
3. **Encode Data** → Convert text to numbers
   - Gender: Male→1, Female→0
   - Married: Yes→1, No→0
   - Education: Graduate→1, NotGraduate→0
4. **Split Data** → 80% training, 20% testing
5. **Train Model** → Logistic Regression learns patterns
6. **Evaluate** → Measure accuracy on test data
7. **Save Model** → Save as model.pkl

### Prediction Process:

1. User submits form
2. Flask receives data
3. Data is encoded using same encoders
4. Model predicts: Approved (Y) or Rejected (N)
5. Confidence score shows probability
6. Result displayed in browser

---

## 📈 Sample Dataset (loan_data.csv)

The dataset includes 30 sample loan records with the following columns:

```
Gender,Married,Dependents,Education,Self_Employed,Applicant_Income,Loan_Amount,Credit_History,Loan_Status
Male,No,0,Graduate,No,5849,2500,1,Y
Female,Yes,1,Graduate,No,4583,5000,1,N
...
```

**Loan_Status**: Y = Approved, N = Rejected

---

## 🛠️ Files Explanation

### `train_model.py`

- Trains the ML model on historical data
- Creates and saves: `model.pkl`, `encoders.pkl`, `le_target.pkl`
- Run this FIRST before running the app
- Includes detailed comments explaining each step

### `app.py`

- Flask backend application
- `/` route: Displays the HTML form
- `/predict` route: Receives form data and returns prediction
- Loads trained model on startup
- Handles data encoding before prediction

### `templates/index.html`

- User interface (frontend)
- HTML form with input fields
- JavaScript handles form submission
- Displays prediction results with animations

### `static/style.css`

- Professional styling with purple gradient theme
- Responsive design (works on mobile/tablet/desktop)
- Clean, modern look
- Animations for user feedback

---

## 🎨 Features

✅ **Simple & Clean UI** - Easy to understand and use  
✅ **Real ML Model** - Uses Logistic Regression  
✅ **Fast Predictions** - Gets result instantly  
✅ **Responsive Design** - Works on all devices  
✅ **Beginner Friendly** - Well-commented code  
✅ **No Errors** - Complete, runnable solution  
✅ **Professional Look** - Gradient styling & animations

---

## 💡 Tips for College Viva

### Key Points to Explain:

1. **Data Science Process**
   - Data collection & cleaning
   - Feature engineering & encoding
   - Model training & evaluation

2. **Machine Learning Algorithm**
   - Why Logistic Regression? (Simple, fast, interpretable)
   - What is accuracy? (% of correct predictions)
   - What are encoders? (Convert text to numbers)

3. **Web Application Flow**
   - Frontend collects user input
   - Backend processes data
   - Model makes prediction
   - Result sent back to frontend

4. **Technologies Used**
   - Flask: Lightweight web framework
   - pandas: Data manipulation
   - scikit-learn: ML algorithms
   - pickle: Save/load models

### Sample Questions & Answers:

**Q: Why save the model as pickle?**  
A: To avoid retraining every time. We train once, save, and load for predictions.

**Q: How does encoding work?**  
A: Converts categorical data (Male/Female) to numbers (1/0) that ML models can understand.

**Q: What if accuracy is low?**  
A: Collect more data, try different features, or use better algorithms.

---

## 🐛 Troubleshooting

### Error: "ModuleNotFoundError: No module named 'flask'"

**Solution:** Run `pip install flask`

### Error: "loan_data.csv not found"

**Solution:** Make sure `loan_data.csv` is in the project root folder

### Error: "model.pkl not found"

**Solution:** Run `python train_model.py` first before `app.py`

### App won't start on localhost:5000

**Solution:**

- Port 5000 might be in use. Change port in app.py:
- `app.run(port=5001)`

### Form not submitting

**Solution:**

- Check browser console (F12)
- Make sure all required fields are filled
- Check if Flask server is running

---

## 📚 Learning Resources

- **Flask Documentation**: https://flask.palletsprojects.com
- **scikit-learn**: https://scikit-learn.org
- **pandas**: https://pandas.pydata.org
- **Python**: https://python.org/learn

---

## 📝 License

This project is for educational purposes. Feel free to modify and use it!

---

## ✨ Next Steps (After College Project)

Once you complete this project, you can:

1. Add more features (co-applicant income, loan term, etc.)
2. Try different ML algorithms (Random Forest, Neural Networks)
3. Deploy to cloud (Heroku, AWS, Azure)
4. Add database to store predictions
5. Build a mobile app version

---

## 📧 Questions?

This project is designed to be beginner-friendly. All code is well-commented!

---

**Happy Learning! 🚀**
