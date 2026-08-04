import streamlit as st
import pandas as pd
import plotly.graph_objects as go


@st.cache_data
def load_data():
    df = pd.read_csv("outputs/daily_sales.csv")

    df["date"] = pd.to_datetime(df["date"])
    return df


def show():

    st.title("📈 Historical Sales Analysis")

    df = load_data()

    # Moving Averages
    df["MA_7"] = df["Sales"].rolling(7).mean()
    df["MA_30"] = df["Sales"].rolling(30).mean()

    fig = go.Figure()

    fig.add_trace(
        go.Scatter(
            x=df["date"],
            y=df["Sales"],
            mode="lines",
            name="Daily Sales"
        )
    )

    fig.add_trace(
        go.Scatter(
            x=df["date"],
            y=df["MA_7"],
            mode="lines",
            name="7-Day Moving Average"
        )
    )

    fig.add_trace(
        go.Scatter(
            x=df["date"],
            y=df["MA_30"],
            mode="lines",
            name="30-Day Moving Average"
        )
    )

    fig.update_layout(
        title="Historical Sales Trend",
        xaxis_title="Date",
        yaxis_title="Sales",
        hovermode="x unified",
        template="plotly_white",
        height=600
    )

    st.plotly_chart(fig, use_container_width=True)

    st.divider()

    st.subheader("Sales Summary")

    c1, c2, c3 = st.columns(3)

    c1.metric("Average Sales", f"{df['Sales'].mean():,.0f}")
    c2.metric("Maximum Sales", f"{df['Sales'].max():,.0f}")
    c3.metric("Minimum Sales", f"{df['Sales'].min():,.0f}")