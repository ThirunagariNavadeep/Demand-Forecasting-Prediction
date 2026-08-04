import streamlit as st

st.set_page_config(
    page_title="Demand Forecasting Dashboard",
    page_icon="📈",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ===========================
# Sidebar
# ===========================

st.sidebar.title("📈 Demand Forecasting Dashboard")
st.sidebar.caption("Machine Learning • Time Series Forecasting")

st.sidebar.markdown("---")

page = st.sidebar.radio(
    "Navigation",
    [
        "🏠 Home",
        "📊 Dataset",
        "📈 Historical Sales",
        "🤖 Model Performance",
        "⭐ Feature Importance",
        "🔮 Forecast",
        "ℹ️ About"
    ]
)

st.sidebar.markdown("---")

st.sidebar.info(
    """
**Project**

- Dataset: M5 Forecasting
- Models: Linear Regression, XGBoost
- Forecast Horizon: 30 Days
"""
)

st.sidebar.markdown("---")

st.sidebar.caption("Developed by Navadeep")

# ===========================
# Routing
# ===========================

PAGES = {
    "🏠 Home": "home",
    "📊 Dataset": "dataset",
    "📈 Historical Sales": "historical",
    "🤖 Model Performance": "models",
    "⭐ Feature Importance": "feature_importance",
    "🔮 Forecast": "forecast",
    "ℹ️ About": "about"
}

module = __import__(f"pages.{PAGES[page]}", fromlist=["show"])
module.show()