import streamlit as st
import pandas as pd
import plotly.express as px
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent


@st.cache_data
def load_forecast():
    return pd.read_csv(BASE_DIR / "outputs" / "forecast.csv")


def show():

    st.title("🔮 30-Day Demand Forecast")

    df = load_forecast()

    df["Date"] = pd.to_datetime(df["Date"])

    # =========================
    # Metrics
    # =========================

    c1, c2, c3 = st.columns(3)

    c1.metric(
        "Average Forecast",
        f"{df['Predicted_Sales'].mean():,.0f}"
    )

    c2.metric(
        "Maximum Forecast",
        f"{df['Predicted_Sales'].max():,.0f}"
    )

    c3.metric(
        "Minimum Forecast",
        f"{df['Predicted_Sales'].min():,.0f}"
    )

    st.divider()

    # =========================
    # Forecast Chart
    # =========================

    fig = px.line(
        df,
        x="Date",
        y="Predicted_Sales",
        markers=True,
        title="30-Day Sales Forecast"
    )

    fig.update_layout(
        height=600,
        xaxis_title="Date",
        yaxis_title="Predicted Sales",
        hovermode="x unified"
    )

    st.plotly_chart(fig, use_container_width=True)

    st.divider()

    # =========================
    # Forecast Table
    # =========================

    st.subheader("Forecast Table")

    st.dataframe(df, use_container_width=True)

    st.divider()

    # =========================
    # Download
    # =========================

    csv = df.to_csv(index=False).encode("utf-8")

    st.download_button(
        label="📥 Download Forecast CSV",
        data=csv,
        file_name="30_day_forecast.csv",
        mime="text/csv"
    )