import streamlit as st
import pandas as pd


@st.cache_data
def load_data():
    return pd.read_csv("D:\Projects\Demand Forecasting Prediction")


def show():

    st.title("📊 Dataset Overview")

    # Load data
    df = load_data()

    st.subheader("Dataset Shape")

    col1, col2 = st.columns(2)

    col1.metric("Rows", df.shape[0])
    col2.metric("Columns", df.shape[1])

    st.divider()

    st.subheader("Column Names")
    st.write(df.columns.tolist())

    st.divider()

    st.subheader("Missing Values")

    missing = df.isnull().sum()

    if missing.sum() == 0:
        st.success("✅ No missing values found.")
    else:
        st.dataframe(
            missing[missing > 0]
            .reset_index()
            .rename(columns={"index": "Column", 0: "Missing Values"}),
            use_container_width=True
        )

    st.divider()

    st.subheader("Dataset Preview")
    st.dataframe(df.head(), use_container_width=True)

    st.divider()

    st.subheader("Summary Statistics")
    st.dataframe(df.describe(), use_container_width=True)
