import streamlit as st
import pickle
import numpy as np

# Load the trained model
@st.cache_resource
def load_model():
    try:
        # Load only the model
        with open("model.pkl", "rb") as file:
            model = pickle.load(file)
        return model
    except pickle.UnpicklingError:
        st.error("Failed to load the model. Ensure the file is a valid pickle file.")
        st.stop()
    except FileNotFoundError:
        st.error("Model file not found. Please check the file path.")
        st.stop()

# Load the model
model = load_model()

# User input section
st.title("Infosys SpringBoard's Stroke Prediction Web Application")
st.sidebar.header("Enter Input Features")

# Collect user inputs for the 10 features (excluding the dummy 11th feature)
gender = st.sidebar.selectbox("Gender", ["Male", "Female"])
age = st.sidebar.number_input("Age", min_value=0, value=30)
hypertension = st.sidebar.selectbox("Hypertension", ["No", "Yes"])
heart_disease = st.sidebar.selectbox("Heart Disease", ["No", "Yes"])
ever_married = st.sidebar.selectbox("Ever Married", ["No", "Yes"])
work_type = st.sidebar.selectbox("Work Type", ["Private", "Self-employed", "Govt_job", "children", "Never_worked"])
residence_type = st.sidebar.selectbox("Residence Type", ["Urban", "Rural"])
avg_glucose_level = st.sidebar.number_input("Average Glucose Level", min_value=50.0, value=100.0)
bmi = st.sidebar.number_input("Body Mass Index", min_value=10.0, value=25.0)
smoking_status = st.sidebar.selectbox("Smoking Status", ["never smoked", "formerly smoked", "smokes"])

# Encode categorical inputs manually
gender = 1 if gender == "Male" else 0
hypertension = 1 if hypertension == "Yes" else 0
heart_disease = 1 if heart_disease == "Yes" else 0
ever_married = 1 if ever_married == "Yes" else 0
work_type = ["Private", "Self-employed", "Govt_job", "children", "Never_worked"].index(work_type)
residence_type = 1 if residence_type == "Urban" else 0
smoking_status = ["never smoked", "formerly smoked", "smokes"].index(smoking_status)

# Input features (only 10 features, excluding the dummy 11th feature)
inputs = np.array([[gender, age, hypertension, heart_disease, ever_married, work_type, residence_type, avg_glucose_level, bmi, smoking_status]])

# Add the dummy 11th feature with a constant value of 0 (assuming this is the expected behavior)
inputs_with_dummy = np.hstack([inputs, np.zeros((inputs.shape[0], 1))])  # Add the dummy feature (constant value 0)

# Button to trigger calculations
if st.button("Calculate Prediction"):
    try:
        # Prediction for user input (whether stroke will occur or not)
        prediction = model.predict(inputs_with_dummy)  # Predict using the model
        prediction_class = "Stroke" if prediction[0] == 1 else "No Stroke"
        
        st.subheader("Prediction Result")
        st.write(f"The predicted outcome is: **{prediction_class}**")

        # Display the inputs and predicted output
        st.subheader("User Input Features")
        st.write(f"- **Gender**: {'Male' if gender == 1 else 'Female'}")
        st.write(f"- **Age**: {age}")
        st.write(f"- **Hypertension**: {'Yes' if hypertension == 1 else 'No'}")
        st.write(f"- **Heart Disease**: {'Yes' if heart_disease == 1 else 'No'}")
        st.write(f"- **Ever Married**: {'Yes' if ever_married == 1 else 'No'}")
        st.write(f"- **Work Type**: {['Private', 'Self-employed', 'Govt_job', 'children', 'Never_worked'][work_type]}")
        st.write(f"- **Residence Type**: {'Urban' if residence_type == 1 else 'Rural'}")
        st.write(f"- **Average Glucose Level**: {avg_glucose_level}")
        st.write(f"- **BMI**: {bmi}")
        st.write(f"- **Smoking Status**: {['never smoked', 'formerly smoked', 'smokes'][smoking_status]}")

    except Exception as e:
        st.error(f"An error occurred: {str(e)}")
