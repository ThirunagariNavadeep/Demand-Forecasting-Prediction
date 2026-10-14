from pathlib import Path
import pandas as pd
import streamlit as st

DATA_PATH = Path(__file__).resolve().parent.parent / "sales_train_evaluation.csv"

@st.cache_data
def load_data():
    if not DATA_PATH.is_file():
        st.error(f"Dataset not found: {DATA_PATH}")
        st.stop()
    return pd.read_csv(DATA_PATH)


def show():
    df = load_data()

    st.title("Dataset Overview")
    st.write("Explore your sales dataset.")
    st.dataframe(df.head())
    st.write("Dataset shape:", df.shape)
