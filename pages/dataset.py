
import pandas as pd
import streamlit as st

DATA_URL = "https://huggingface.co/datasets/Navadeep018/Sales/resolve/main/sales_train_evaluation.csv"

@st.cache_data
def load_data():
    return pd.read_csv(DATA_URL)

