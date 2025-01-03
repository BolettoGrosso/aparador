import streamlit as st
import pandas as pd

# URL of the public Google Sheet in CSV format
sheet_url = 'https://docs.google.com/spreadsheets/d/1Hu2Rl6QE6-Fd_MeP2M4Ffb6Xzcmwm8cJ1p6QwsJa0fs/export?format=csv'

# Read data from the Google Sheet
@st.cache_data
def load_data():
    data = pd.read_csv(sheet_url)
    # Debugging: Show all columns to identify the correct names
    # Replace these with the correct column names based on the output above
    columns_to_display = ["Identificador", "Fecha de conclusión", "Valor subasta", "Provincia_lot'"]  # Replace with real names
    data = data[columns_to_display]
    return data

# Load the dataset
st.title('Subastas disponibles')
data = load_data()

# Display the first 10 rows
st.write('### First 10 Rows of the Dataset')
st.dataframe(data.head(10))
