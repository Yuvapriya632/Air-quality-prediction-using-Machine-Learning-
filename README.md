# 🌍 Air Quality Prediction Using LSTM

Air Quality Prediction System using Deep Learning and LSTM .A web-based application that uses Long Short-Term Memory (LSTM) networks to predict air quality from historical air pollution data.

---

## 📌 1. Project Overview

Air pollution is one of the major environmental challenges affecting human health and the quality of life. Monitoring and predicting air quality can help people understand pollution levels and take preventive measures.

**Air Quality Prediction Using LSTM** is a Deep Learning project developed to predict air quality using historical air pollution data. The project implements a Long Short-Term Memory (LSTM) neural network, which is a type of Recurrent Neural Network (RNN) designed to learn patterns and relationships in sequential data.

The trained LSTM model is integrated into a web application developed using Python and Flask. Users can interact with the application, enter the required information, and obtain air quality predictions.

### Main Objectives

- Analyze historical air quality and pollution data.
- Perform data preprocessing and transformation.
- Develop a Deep Learning model using LSTM.
- Train and evaluate the prediction model.
- Integrate the trained model into a web application.
- Provide a simple interface for users to obtain predictions.
- Store user registration information using SQLite.

---

## 🎥 2. Project Demonstration

Watch the complete project demonstration to understand the application interface and prediction process.

**YouTube Demo:**

[▶️ Watch Air Quality Prediction Project Demo](https://youtu.be/0Md1vNBAM7Y?si=ueOMu1ztlhjHm9MI)

---

## 📊 3. Dataset

The dataset used for this project is available on Kaggle.

**Dataset Name:** Air Quality Prediction Using Machine Learning

[📥 View and Download the Dataset on Kaggle](https://www.kaggle.com/datasets/yuvashrisankar/air-quality-prediction-using-ml)

### Dataset Usage

The dataset is used for:

- Loading historical air quality information.
- Exploring and understanding the available data.
- Identifying relevant features.
- Preparing data for model training.
- Transforming the data into a suitable format for LSTM.
- Training and testing the prediction model.

### Dataset Files

| File | Purpose |
|---|---|
| `data.csv` | Main dataset used for data analysis and model development |
| `input.csv` | Additional input data file generated during data processing |

---

## 🧠 4. Deep Learning Model – LSTM

### What is LSTM?

Long Short-Term Memory (LSTM) is a special type of Recurrent Neural Network (RNN) that is widely used for sequential and time-series prediction problems.

Unlike traditional neural networks, LSTM can retain information from previous time steps and use it to understand patterns in sequential data.

LSTM uses three main gates:

**1. Forget Gate**

Determines which information from the previous cell state should be removed.

**2. Input Gate**

Determines which new information should be stored in the cell state.

**3. Output Gate**

Determines what information should be passed to the next hidden state.

### Why LSTM?

LSTM is suitable for this project because:

- It can learn patterns from sequential data.
- It can capture relationships between previous and current observations.
- It can retain useful information over multiple time steps.
- It is commonly used for time-series forecasting applications.

### Model Files

The trained model and preprocessing objects are stored in the `Model` directory.

| File Name | Description |
|---|---|
| `lstm_aqi_model.h5` | Saved and trained LSTM Deep Learning model |
| `scaler.pkl` | Saved data scaler used during preprocessing |
| `label_encoder.pkl` | Saved label encoder used for categorical data encoding |

These files are loaded by the application to process input data and generate predictions.

---

## ⚙️ 5. Technologies and Tools Used

| Technology | Purpose |
|---|---|
| Python | Main programming language |
| TensorFlow | Deep Learning framework |
| Keras | Building and loading the LSTM model |
| LSTM | Sequential data prediction |
| Pandas | Data manipulation and analysis |
| NumPy | Numerical operations |
| Scikit-learn | Data preprocessing and transformation |
| Flask | Backend web application framework |
| HTML | Web page structure |
| CSS | Web page styling |
| SQLite | User information storage |
| Jupyter Notebook | Model development and experimentation |
| Visual Studio Code | Development environment |

---

## ✨ 6. Key Features

### 6.1 User Registration

- New users can register through the signup page.
- User information is stored in the SQLite database.
- Provides an entry point to the prediction application.

### 6.2 User Login

- Registered users can access the application through the login page.
- Provides a user authentication interface.

### 6.3 Home Page

- Provides an introduction to the air quality prediction application.
- Displays the main application interface.
- Allows users to navigate to the prediction functionality.

### 6.4 Air Quality Prediction

- Accepts the required prediction inputs through the web interface.
- Uses the saved preprocessing objects to prepare input data.
- Loads the trained LSTM model.
- Generates and displays the prediction result.

### 6.5 Prediction Results

- Displays the prediction generated by the trained model.
- Provides an easy-to-understand result interface.

---

## 🔄 7. Project Workflow

The overall workflow of the project is as follows:

```text
        Historical Air Quality Dataset
                     |
                     v
              Data Collection
                     |
                     v
             Data Preprocessing
                     |
                     v
             Feature Preparation
                     |
                     v
              Data Scaling
                     |
                     v
              LSTM Model
                     |
                     v
               Model Training
                     |
                     v
              Trained Model
                     |
                     v
            Save Model Files
                     |
                     v
             Flask Integration
                     |
                     v
              Web Application
                     |
                     v
              User Input
                     |
                     v
             Data Transformation
                     |
                     v
              LSTM Prediction
                     |
                     v
              Display Results
```

### Workflow Explanation

1. **Data Collection:** Historical air quality data is loaded from the CSV dataset.
2. **Data Preprocessing:** The dataset is prepared for model development.
3. **Feature Preparation:** Relevant input features are selected and transformed.
4. **Data Scaling:** Numerical data is scaled using the preprocessing approach used during model training.
5. **Model Training:** An LSTM model is developed and trained using the prepared data.
6. **Model Saving:** The trained model and preprocessing objects are saved as files.
7. **Flask Integration:** The saved model is integrated into the Flask application.
8. **User Interaction:** Users enter the required information through the web interface.
9. **Prediction:** The application processes the input and generates a prediction.
10. **Result Display:** The prediction is displayed on the result page.

---

## 📂 8. Project Folder Structure

```text
Air-Quality-Prediction/
│
├── Air Quality - Lstm/
│   │
│   ├── Backend/
│   │   ├── air_quality_prediction.ipynb
│   │   ├── data.csv
│   │   └── input.csv
│   │
│   └── frontend/
│       │
│       ├── Model/
│       │   ├── label_encoder.pkl
│       │   ├── lstm_aqi_model.h5
│       │   ├── scaler.pkl
│       │
│       ├── static/
│       │   ├── 1.jpg
│       │   ├── ain.jpg
│       │   ├── alogin.jpg
│       │   ├── are.jpg
│       │   └── asign.png
│       │
│       ├── templates/
│       │   ├── home.html
│       │   ├── login.html
│       │   ├── predict.html
│       │   ├── result.html
│       │   └── signup.html
│       │
│       ├── app.py
│       └── users.db
│
└── README.md
```

### Folder Description

| Folder/File | Description |
|---|---|
| `Backend/` | Contains the Jupyter Notebook and dataset files |
| `frontend/` | Contains the web application |
| `Model/` | Stores the trained model and preprocessing objects |
| `static/` | Contains application images and static assets |
| `templates/` | Contains HTML pages |
| `app.py` | Main Flask application |
| `users.db` | SQLite database for user information |
| `air_quality_prediction.ipynb` | Notebook containing model development and data analysis |

---

## 💻 9. Source Code

The complete source code is available on GitHub.

[🔗 GitHub Repository – Air Quality Prediction Using Machine Learning](https://github.com/Yuvapriya632/Air-quality-prediction-using-Machine-Learning-)

You can clone the repository to access the project files.

---

## 🚀 10. Installation and Setup

Follow the instructions below to run the project locally.

### Prerequisites

Make sure you have installed:

- Python
- pip package manager
- Git
- Visual Studio Code (recommended)

### Step 1: Clone the Repository

Open your terminal or PowerShell and execute:

```bash
git clone https://github.com/Yuvapriya632/Air-quality-prediction-using-Machine-Learning-.git
```

### Step 2: Navigate to the Project Directory

```bash
cd Air-quality-prediction-using-Machine-Learning-
```

### Step 3: Navigate to the Application Folder

```bash
cd "Air Quality - Lstm/frontend"
```

### Step 4: Create a Virtual Environment (Recommended)

```bash
py -m venv venv
```

Activate the virtual environment on Windows:

```powershell
.\venv\Scripts\Activate.ps1
```

If PowerShell blocks activation, you can use Command Prompt:

```cmd
venv\Scripts\activate
```

### Step 5: Install Required Dependencies

```bash
py -m pip install --upgrade pip
```

Install the required Python libraries:

```bash
py -m pip install flask tensorflow pandas numpy scikit-learn joblib
```

**Note:** TensorFlow installation compatibility depends on your Python version and operating system.

### Step 6: Run the Flask Application

```bash
py app.py
```

### Step 7: Access the Application

Open your browser and visit:

```text
http://127.0.0.1:5000/
```

The application will be available locally if Flask starts successfully on port 5000.

---

## 📈 11. Model Development

The Jupyter Notebook is available at:

`Backend/air_quality_prediction.ipynb`

The notebook contains the model development process, including:

- Dataset loading.
- Data exploration.
- Data preprocessing.
- Feature preparation.
- Data transformation.
- LSTM model development.
- Model training.
- Saving the trained model and preprocessing objects.

The trained model is saved as:

`lstm_aqi_model.h5`

The saved model is subsequently used by the web application.

---

## 🛠️ 12. Troubleshooting

### Issue 1: TensorFlow Not Found

Error:

```text
ModuleNotFoundError: No module named 'tensorflow'
```

Solution:

```bash
py -m pip install tensorflow
```

### Issue 2: Flask Not Found

Error:

```text
ModuleNotFoundError: No module named 'flask'
```

Solution:

```bash
py -m pip install flask
```

### Issue 3: Model File Not Found

Make sure the following files are available in the `Model` folder:

```text
lstm_aqi_model.h5
scaler.pkl
label_encoder.pkl
```

Also verify that the paths used in `app.py` match the actual folder structure.

### Issue 4: Application Not Opening

- Verify that the Flask application is running.
- Check the terminal for errors.
- Confirm the correct local URL and port.
- Make sure all required dependencies are installed.

---

## 🔮 13. Future Enhancements

The project can be further improved with the following features:

- Integration with real-time air quality monitoring APIs.
- Live AQI data collection.
- Improved LSTM model performance through hyperparameter tuning.
- Interactive dashboards for air quality visualization.
- Location-based air quality prediction.
- Historical air quality trend analysis.
- Deployment using cloud platforms.
- Mobile-friendly user interface.
- Air pollution alerts and notifications.

---

## 🎯 14. Applications

This project can be useful in the following areas:

- Environmental monitoring.
- Air pollution analysis.
- Smart city applications.
- Public health awareness.
- Environmental research.
- Predictive analytics.

---

## 👩‍💻 15. Author

**Yuvapriya S**

AI / ML Developer | Machine Learning | Deep Learning | Data Science

**Professional Profiles:**

- GitHub: [Yuvapriya632](https://github.com/Yuvapriya632)
- Kaggle: [yuvashrisankar](https://www.kaggle.com/yuvashrisankar)

---

## 🔗 16. Project Links

| Resource | Link |
|---|---|
| Project Demo | [Watch on YouTube](https://youtu.be/0Md1vNBAM7Y?si=ueOMu1ztlhjHm9MI) |
| Dataset | [Kaggle Dataset](https://www.kaggle.com/datasets/yuvashrisankar/air-quality-prediction-using-ml) |
| Source Code | [GitHub Repository](https://github.com/Yuvapriya632/Air-quality-prediction-using-Machine-Learning-) |

---

## ⭐ Support

If you find this project useful or interesting, please consider giving the GitHub repository a ⭐ star.

Thank you for visiting this project!
