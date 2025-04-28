import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os

def show():
    # Get the correct path relative to the script
    current_dir = os.path.dirname(os.path.abspath(__file__))
    csv_path = os.path.join(current_dir, 'pima_indians_diabetes.csv')

    # Now read the CSV
    df = pd.read_csv(csv_path)

    st.title("Explore Dataset")

    st.subheader("Raw Dataset")
    st.dataframe(df.head(20))

    st.subheader("Statistical Summary")
    st.write(df.describe())

    st.subheader("Class Distribution")
    sns.countplot(x='Outcome', data=df)
    st.pyplot(plt)
