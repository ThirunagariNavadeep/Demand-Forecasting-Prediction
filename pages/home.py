import streamlit as st

def show():

    
    st.title("📈 Demand Forecasting Dashboard")
    st.caption("Machine Learning • Time Series Forecasting • M5 Forecasting Dataset")
    st.image("assets/banner.png", use_container_width=True)

    st.markdown("---")

    # =========================
    # KPI Cards
    # =========================

    c1, c2, c3, c4 = st.columns(4)

    c1.metric("🏆 Best Model", "Linear Regression")
    c2.metric("📊 R² Score", "0.7104")
    c3.metric("📅 Forecast", "30 Days")
    c4.metric("📦 Dataset", "M5")

    st.markdown("---")

    left, right = st.columns([2, 1])

    with left:

        st.subheader("📖 Project Overview")

        st.write("""
This project forecasts future product demand using historical sales data from the
**M5 Forecasting Dataset**.

The workflow includes:

- Data Cleaning
- Exploratory Data Analysis
- Time Series Analysis
- Feature Engineering
- Model Training
- Hyperparameter Tuning
- Model Evaluation
- 30-Day Demand Forecasting
""")

    with right:

        st.subheader("🛠 Tech Stack")

        st.success("Python")
        st.success("Pandas")
        st.success("Scikit-Learn")
        st.success("XGBoost")
        st.success("Plotly")
        st.success("Streamlit")

    st.markdown("---")

    st.subheader("📌 Workflow")

    st.markdown("""
```text
Historical Sales
        │
        ▼
Data Cleaning
        │
        ▼
Feature Engineering
        │
        ▼
Model Training
        │
        ▼
Hyperparameter Tuning
        │
        ▼
Evaluation
        │
        ▼
30-Day Forecast
""")