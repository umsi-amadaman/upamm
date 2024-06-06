import streamlit as st

# Title of the application
st.title("Dynamic Form Example")

# Sidebar for dynamic form selection
st.sidebar.title("Form Options")
form_type = st.sidebar.selectbox("Choose form type", ["Contact Form", "Survey Form"])

# Function to create a contact form
def create_contact_form():
    st.header("Contact Form")
    name = st.text_input("Name")
    email = st.text_input("Email")
    message = st.text_area("Message")
    
    if st.button("Submit"):
        st.write(f"Name: {name}")
        st.write(f"Email: {email}")
        st.write(f"Message: {message}")

# Function to create a survey form
def create_survey_form():
    st.header("Survey Form")
    age = st.number_input("Age", min_value=0, max_value=100, step=1)
    gender = st.selectbox("Gender", ["Male", "Female", "Other"])
    feedback = st.text_area("Feedback")
    
    if st.button("Submit"):
        st.write(f"Age: {age}")
        st.write(f"Gender: {gender}")
        st.write(f"Feedback: {feedback}")

# Display the selected form
if form_type == "Contact Form":
    create_contact_form()
elif form_type == "Survey Form":
    create_survey_form()
