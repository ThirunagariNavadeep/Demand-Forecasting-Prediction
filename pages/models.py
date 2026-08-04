import streamlit as st
import pandas as pd
import plotly.express as px
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent


@st.cache_data
def load_metrics():
    return pd.read_csv(BASE_DIR / "outputs" / "metrics.csv")


def show():
    st.title("🤖 Model Performance")

    df = load_metrics()

    st.subheader("Performance Comparison")
    st.dataframe(df, use_container_width=True)

    col1, col2 = st.columns(2)

    with col1:
        fig = px.bar(
            df,
            x="Model",
            y="MAE",
            title="MAE Comparison",
            text_auto=".2f"
        )
        st.plotly_chart(fig, use_container_width=True)

    with col2:
        fig = px.bar(
            df,
            x="Model",
            y="R2",
            title="R² Comparison",
            text_auto=".3f"
        )
        st.plotly_chart(fig, use_container_width=True)

    best = df.loc[df["R2"].idxmax()]

    st.success(
        f"🏆 Best Overall Model: **{best['Model']}** (R² = {best['R2']:.4f})"
    )