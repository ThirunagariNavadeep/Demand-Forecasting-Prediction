# 📈 Demand Forecasting using Machine Learning

An end-to-end Machine Learning project that forecasts future product demand using historical sales data from the **M5 Forecasting Dataset**. The project includes data preprocessing, feature engineering, model training, hyperparameter tuning, model evaluation, and an interactive Streamlit dashboard for visualization and forecasting.

---

## 📌 Project Overview

Demand forecasting plays a critical role in inventory management, production planning, logistics, and supply chain optimization.

This project builds a demand forecasting pipeline capable of predicting future sales using historical data and engineered time-series features.

### Key Features

- 📊 Exploratory Data Analysis (EDA)
- 📅 Time Series Analysis
- ⚙️ Feature Engineering
- 🤖 Multiple Machine Learning Models
- 🎯 Hyperparameter Tuning
- ⭐ Feature Importance Analysis
- 🔮 30-Day Sales Forecast
- 📈 Interactive Streamlit Dashboard

---

## 🎯 Business Problem

Businesses need accurate demand forecasts to:

- Optimize inventory levels
- Reduce stock shortages
- Minimize overstocking costs
- Improve production planning
- Enhance supply chain efficiency
- Support data-driven business decisions

---

## 📂 Dataset

**Dataset:** M5 Forecasting Accuracy Dataset

Files Used:

- `sales_train_evaluation.csv`
- `calendar.csv`
- `sell_prices.csv`

The dataset contains daily sales information collected from multiple Walmart stores across different product categories.

---

## 🛠 Tech Stack

### Programming Language

- Python

### Libraries

- Pandas
- NumPy
- Matplotlib
- Plotly
- Scikit-Learn
- XGBoost
- Joblib
- Streamlit

---

## 📊 Exploratory Data Analysis

Performed:

- Missing Value Analysis
- Data Inspection
- Time Series Visualization
- Trend Analysis
- Seasonal Decomposition
- Sales Distribution Analysis

---

## ⚙️ Feature Engineering

The following features were created to improve forecasting performance:

### Lag Features

- Lag_1
- Lag_30

### Rolling Statistics

- Rolling Mean (7 Days)
- Rolling Mean (30 Days)
- Rolling Standard Deviation (7 Days)

### Calendar Features

- Year
- Month
- Day
- Day of Week
- Weekend Indicator

---

## 🤖 Machine Learning Models

The following models were trained and evaluated:

- Linear Regression
- XGBoost
- Tuned XGBoost

Hyperparameter tuning was performed using:

- RandomizedSearchCV
- TimeSeriesSplit Cross Validation

---

## 📈 Model Performance

| Model | MAE | RMSE | R² Score |
|------|------:|------:|------:|
| Linear Regression | **2530.74** | **3638.54** | **0.7104** |
| Default XGBoost | 2538.94 | 3850.79 | 0.6756 |
| Tuned XGBoost | **2257.72** | 3710.20 | 0.6989 |

### Key Observations

- Linear Regression achieved the highest R² score and lowest RMSE.
- Hyperparameter tuning significantly improved XGBoost performance, reducing the MAE compared to the default model.
- Feature engineering substantially improved forecasting accuracy.

---

## ⭐ Feature Importance

The tuned XGBoost model identified the following features as the most influential:

| Feature | Importance |
|----------|-----------:|
| Lag_1 | 0.349 |
| DayOfWeek | 0.303 |
| Rolling_Mean_7 | 0.225 |
| Rolling_STD_7 | 0.037 |
| Lag_30 | 0.037 |
| Month | 0.018 |
| Rolling_Mean_30 | 0.017 |
| Year | 0.015 |

---

## 🔮 Future Forecasting

The project generates a **30-day recursive demand forecast** using the trained machine learning model.

The forecast includes:

- Future sales predictions
- Interactive visualization
- Downloadable forecast CSV

---

## 📊 Streamlit Dashboard

The project includes a fully interactive Streamlit dashboard with the following pages:

- 🏠 Home
- 📈 Historical Sales
- 🤖 Model Performance
- ⭐ Feature Importance
- 🔮 30-Day Forecast
- ℹ️ About

Dashboard Features:

- Interactive Plotly Charts
- KPI Cards
- Model Comparison
- Feature Importance Visualization
- Forecast Table
- Download Forecast CSV

---

## 📁 Project Structure

```
Demand-Forecasting/
│
├── app.py
├── README.md
├── requirements.txt
│
├── model/
│   ├── linear_regression.pkl
│   └── tuned_xgboost.pkl
│
├── outputs/
│   ├── daily_sales.csv
│   ├── metrics.csv
│   ├── feature_importance.csv
│   └── forecast.csv
│
├── pages/
│   ├── home.py
│   ├── historical.py
│   ├── models.py
│   ├── feature_importance.py
│   ├── forecast.py
│   └── about.py
│
├── notebook/
│   └── Demand Forecasting.ipynb
│
├── data/
│
└── images/
```

---

## 🚀 Installation

Clone the repository:

```bash
git clone https://github.com/your-username/Demand-Forecasting.git
```

Navigate to the project directory:

```bash
cd Demand-Forecasting
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the Streamlit application:

```bash
streamlit run app.py
```

---

## 📷 Dashboard Preview

### Home

_Add screenshot here_

### Historical Sales

_Add screenshot here_

### Model Performance

_Add screenshot here_

### Feature Importance

_Add screenshot here_

### Forecast

_Add screenshot here_

---

## 📈 Future Improvements

Potential enhancements include:

- Integration of holiday and event features from `calendar.csv`
- Incorporation of product pricing information from `sell_prices.csv`
- Store-level and product-level demand forecasting
- LSTM and Transformer-based forecasting models
- Prophet model comparison
- Automated model retraining
- Cloud deployment with CI/CD

---

## 👨‍💻 Author

**Navadeep**

- GitHub: https://github.com/ThirunagariNavadeep
- LinkedIn: *(Add your LinkedIn profile)*
- Portfolio: *(Add your portfolio URL)*

---

## ⭐ If you found this project useful, consider giving it a star on GitHub!