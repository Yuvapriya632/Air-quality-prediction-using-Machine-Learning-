from flask import Flask, render_template, request, redirect, url_for, session
import warnings
warnings.filterwarnings("ignore")
import sqlite3
import numpy as np
import joblib
from tensorflow.keras.models import load_model
loaded_model = load_model("Model/lstm_aqi_model.h5")
scaler = joblib.load("Model/scaler.pkl")
label_encoder = joblib.load("Model/label_encoder.pkl")

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Use a strong secret key in production

# Initialize SQLite3 database
def init_db():
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    # Create a table for users if it doesn't already exist
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

@app.route('/')
def index():
    return redirect(url_for('home'))

@app.route('/home')
def home():
    return render_template('home.html')

# Decorator to ensure user is logged in
def login_required(route_function):
    def wrapper(*args, **kwargs):
        if 'user_id' not in session:
            return redirect(url_for('login'))
        return route_function(*args, **kwargs)
    wrapper.__name__ = route_function.__name__
    return wrapper

# Signup route
@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        try:
            # Save new user in SQLite3 database
            conn = sqlite3.connect('users.db')
            cursor = conn.cursor()
            cursor.execute('INSERT INTO users (username, password) VALUES (?, ?)', (username, password))
            conn.commit()
            conn.close()
            return redirect(url_for('login'))
        except sqlite3.IntegrityError:
            return 'Username already exists. Please choose another one.'
    return render_template('signup.html')

# Login route
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        # Verify user credentials
        conn = sqlite3.connect('users.db')
        cursor = conn.cursor()
        cursor.execute('SELECT id FROM users WHERE username = ? AND password = ?', (username, password))
        user = cursor.fetchone()
        conn.close()
        if user:
            session['user_id'] = user[0]  # Store user ID in session
            return redirect(url_for('predict'))
        else:
            return 'Invalid username or password'
    return render_template('login.html')

# Logout route
@app.route('/logout')
def logout():
    session.pop('user_id', None)  # Remove user ID from session
    return redirect(url_for('home'))

def prediction(SOi,Noi,Rpi,SPMi):
    new_data = np.array([[SOi,Noi,Rpi,SPMi]])
    new_data_scaled = scaler.transform(new_data)
    new_data_reshaped = new_data_scaled.reshape(1, 1, new_data.shape[1])
    prediction = loaded_model.predict(new_data_reshaped)
    predicted_class = np.argmax(prediction) 
    prediction = label_encoder.inverse_transform([predicted_class]) 
    
    return prediction[0]

# Prediction route
@app.route('/predict', methods=['GET', 'POST'])
@login_required
def predict():
    if request.method == 'POST':
        SOi = float(request.form['SOi'])
        Noi = float(request.form['Noi'])
        Rpi = float(request.form['Rpi'])
        SPMi = float(request.form['SPMi'])
    
        # Predict loan approval
        prediction_result = prediction(SOi,Noi,Rpi,SPMi)
        return render_template('result.html', prediction=prediction_result)

    return render_template('predict.html')


if __name__ == '__main__':
    init_db() 
    app.run(debug=True)
