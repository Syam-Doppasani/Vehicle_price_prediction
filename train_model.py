# train_model.py

import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.ensemble import RandomForestRegressor
from sklearn.impute import SimpleImputer

# Load dataset
df = pd.read_csv('vehicles.csv')

# Drop rows with missing target or essential features
df = df.dropna(subset=['price', 'engine'])

# Feature selection
features = ['make', 'model', 'year', 'mileage', 'fuel', 'transmission', 'body', 'drivetrain', 'engine']
target = 'price'
X = df[features]
y = df[target]

# Preprocessing
categorical = ['make', 'model', 'fuel', 'transmission', 'body', 'drivetrain', 'engine']
numerical = ['year', 'mileage']

preprocessor = ColumnTransformer(transformers=[
    ('cat', OneHotEncoder(handle_unknown='ignore'), categorical),
    ('num', SimpleImputer(strategy='mean'), numerical)
])

# Pipeline
pipeline = Pipeline(steps=[
    ('preprocessor', preprocessor),
    ('model', RandomForestRegressor(n_estimators=100, random_state=42))
])

# Train/test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Fit the model
pipeline.fit(X_train, y_train)

# Save the model
joblib.dump(pipeline, 'vehicle_price_model.pkl')
print("Model trained and saved!")
