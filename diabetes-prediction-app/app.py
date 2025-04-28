import streamlit as st
import overview
import explore_data
import model_training
import prediction

# Set Streamlit page configuration
st.set_page_config(
    page_title="Diabetes Prediction System",
    page_icon="🩺",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Sidebar Navigation
st.sidebar.title("🔎 Diabetes Prediction Web App")
st.sidebar.markdown("Navigate through different sections:")

page = st.sidebar.radio(
    "Select a Page:",
    ("Overview", "Explore Data", "Model Training", "Prediction")
)

# Main Area
try:
    if page == "Overview":
        overview.show()
    elif page == "Explore Data":
        explore_data.show()
    elif page == "Model Training":
        model_training.show()
    elif page == "Prediction":
        prediction.show()
    else:
        st.error("Invalid page selection. Please try again from the sidebar.")
except Exception as e:
    st.error(f"An unexpected error occurred: {e}")
