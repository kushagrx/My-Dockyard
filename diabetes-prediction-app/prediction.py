def show():
    import streamlit as st
    import numpy as np
    import pandas as pd
    from sklearn.ensemble import RandomForestClassifier

    st.title("Make a Prediction")
    st.markdown("Fill the values below to predict diabetes risk.")

    pregnancies = st.number_input("Pregnancies", 0, 20, 1)
    glucose = st.number_input("Glucose", 0, 200, 110)
    bp = st.number_input("Blood Pressure", 0, 150, 70)
    skin = st.number_input("Skin Thickness", 0, 100, 20)
    insulin = st.number_input("Insulin", 0, 900, 79)
    bmi = st.number_input("BMI", 0.0, 70.0, 24.0)
    dpf = st.number_input("Diabetes Pedigree Function", 0.0, 2.5, 0.5)
    age = st.number_input("Age", 1, 120, 33)

    input_data = np.array([[pregnancies, glucose, bp, skin, insulin, bmi, dpf, age]])

    if st.button("Predict"):
        df = pd.read_csv("pima_indians_diabetes.csv")
        X = df.drop("Outcome", axis=1)
        y = df["Outcome"]
        model = RandomForestClassifier()
        model.fit(X, y)

        prediction = model.predict(input_data)
        st.success("Positive for Diabetes" if prediction[0] == 1 else "Negative for Diabetes")
