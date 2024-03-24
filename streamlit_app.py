import streamlit as st
import pandas as pd

# Main title for the dashboard
st.title("New Zealand Migration Trends")

@st.cache_data  # Use Streamlit's cache to load the data only once
df = pd.read_pickle("df_citizenship_direction_202312.pkl")
