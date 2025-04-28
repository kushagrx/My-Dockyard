def show():
    import streamlit as st
    import pandas as pd
    from sklearn.model_selection import train_test_split
    from sklearn.ensemble import RandomForestClassifier
    from sklearn.linear_model import LogisticRegression
    from sklearn.tree import DecisionTreeClassifier
    from sklearn.svm import SVC
    from sklearn.metrics import classification_report, accuracy_score
    import os

# Get the correct path relative to the script
    current_dir = os.path.dirname(os.path.abspath(__file__))
    csv_path = os.path.join(current_dir, 'pima_indians_diabetes.csv')

# Now read the CSV
    df = pd.read_csv(csv_path)

    st.title("Model Training & Evaluation")
    X = df.drop("Outcome", axis=1)
    y = df["Outcome"]

    model_choice = st.selectbox("Choose Model", ("Logistic Regression", "Decision Tree", "Random Forest", "SVM"))

    test_size = st.slider("Test Set Size", 0.1, 0.5, 0.2)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=42)

    if st.button("Train Model"):
        if model_choice == "Logistic Regression":
            model = LogisticRegression(max_iter=1000)
        elif model_choice == "Decision Tree":
            model = DecisionTreeClassifier()
        elif model_choice == "Random Forest":
            model = RandomForestClassifier()
        else:
            model = SVC()

        model.fit(X_train, y_train)
        y_pred = model.predict(X_test)

        acc = accuracy_score(y_test, y_pred)
        st.success(f"Model Accuracy: {acc:.2f}")
        st.text("Classification Report:")
        st.text(classification_report(y_test, y_pred))
