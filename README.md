# 🚗 Vehicle Price Prediction System

This project is a machine learning-based web application that predicts vehicle prices based on user-input vehicle specifications such as make, model, year, engine type, mileage, and more.

It consists of:
- A Python script for training a regression model using historical vehicle data.
- A user-friendly **Streamlit** interface that allows users to input vehicle details and get instant price predictions.

---

## 📌 Features

- Predicts vehicle prices based on:
  - Make & Model
  - Year
  - Engine
  - Mileage
  - Fuel Type
  - Transmission
  - Body Style
  - Drivetrain
- Streamlit-based UI for easy interaction
- Trained using Random Forest Regressor for high performance

---

## 🧠 Machine Learning Pipeline

- **Preprocessing**:
  - One-hot encoding for categorical variables
  - Simple imputation for missing numerical values
- **Model**:
  - Random Forest Regressor (`sklearn.ensemble`)
- **Evaluation**:
  - Train/test split (80/20)
  - Metrics: MAE, RMSE, R² (can be added in later versions)

---

## 🛠️ Installation & Setup

1. **Clone the repository:**



2. **Install required packages:**
pip install -r requirements.txt

3. **Prepare your dataset:**
[vehicles.csv](https://github.com/user-attachments/files/20465532/vehicles.csv)

4. **Train the model:**
python train_model.py

5. **Run the Streamlit app:**
streamlit run app.py

## 📁 Project Structure

vehicle-price-predictor/
├── vehicles.csv                 # Dataset file
├── train_model.py              # Script to preprocess data and train model
├── app.py                      # Streamlit app for predictions
├── vehicle_price_model.pkl     # Saved trained model
├── README.md                   # Project documentation
└── requirements.txt            # Dependencies

## 📊 Example Screenshot

![Screenshot 2025-05-28 011931](https://github.com/user-attachments/assets/692314b2-63fd-4291-a25c-92ddc6cdcd82)

## 📌 Dependencies
pandas

scikit-learn

streamlit

joblib

Install all with:
[requirements.txt](https://github.com/user-attachments/files/20465618/requirements.txt)

# 👨‍💻 Author
Syam Doppasani

For freelance work or collaborations: syamdoppasani@gmail.com

