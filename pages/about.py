import streamlit as st


def show():

    st.title("ℹ️ About Project")

    st.markdown("""
# Demand Forecasting using Machine Learning

## Business Problem

Accurate demand forecasting helps organizations optimize inventory,
production planning, logistics, and supply chain operations.

## Dataset

- M5 Forecasting Dataset
- Daily Sales Data

## Models Used

- Linear Regression
- XGBoost
- Hyperparameter Tuning (RandomizedSearchCV + TimeSeriesSplit)

## Feature Engineering

- Lag Features
- Rolling Mean
- Rolling Standard Deviation
- Calendar Features

## Evaluation Metrics

- MAE
- RMSE
- R² Score

## Forecast

- 30-Day Recursive Forecast

## Tech Stack

- Python
- Pandas
- Scikit-learn
- XGBoost
- Plotly
- Streamlit

---

Developed by **Navadeep**
""")