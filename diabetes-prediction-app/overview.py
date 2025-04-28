def show():
    import streamlit as st

    st.title("ML for Healthcare: Predicting Diabetes")
    st.markdown("""
    ### Project Overview
    Diabetes is a chronic disease that can lead to severe health issues if not diagnosed early. In this project, we use
    machine learning models to predict the likelihood of a patient having diabetes based on diagnostic medical attributes.

    This application allows users to:
    - Explore the dataset used for training the models
    - Train and evaluate different ML classifiers
    - Make predictions based on input features

    **Dataset Source:** [Pima Indians Diabetes Dataset](https://www.kaggle.com/datasets/uciml/pima-indians-diabetes-database)
    """)

    st.info("Use the sidebar to navigate through different stages of the project.")
