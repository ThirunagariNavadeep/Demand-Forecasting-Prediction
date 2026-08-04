import streamlit as st
import pandas as pd
import plotly.express as px
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent


@st.cache_data
def load_data():
    return pd.read_csv(BASE_DIR / "outputs" / "feature_importance.csv")


def show():

    st.title("⭐ Feature Importance")

    df = load_data()

    # Sort by importance
    df = df.sort_values("Importance", ascending=True)

    st.subheader("Feature Importance")

    fig = px.bar(
        df,
        x="Importance",
        y="Feature",
        orientation="h",
        text="Importance",
        color="Importance",
        color_continuous_scale="Blues"
    )

    fig.update_layout(
        height=600,
        xaxis_title="Importance Score",
        yaxis_title="Feature",
        coloraxis_showscale=False
    )

    st.plotly_chart(fig, use_container_width=True)

    st.divider()

    st.subheader("Feature Importance Table")

    st.dataframe(
        df.sort_values("Importance", ascending=False),
        use_container_width=True
    )

    st.divider()

    st.info(
        """
        **Key Insights**

        - Lag_1 is the most influential feature.
        - DayOfWeek captures weekly demand patterns.
        - Rolling Mean (7 days) helps identify recent trends.
        - Quarter and Lag_7 were removed because they contributed little to the model.
        """
    )