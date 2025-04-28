def show():
    import streamlit as st
    import pandas as pd
    import seaborn as sns
    import matplotlib.pyplot as plt

    st.title("Explore Dataset")
    df = pd.read_csv("pima_indians_diabetes.csv")

    st.subheader("Raw Dataset")
    st.dataframe(df.head(20))

    st.subheader("Statistical Summary")
    st.write(df.describe())

    st.subheader("Class Distribution")
    sns.countplot(x='Outcome', data=df)
    st.pyplot(plt)