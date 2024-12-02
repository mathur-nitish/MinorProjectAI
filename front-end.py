import streamlit as st
import requests


# streamlit run app.py

st.title("Speed Sense")

start_location = st.text_input("Enter Start Location")
end_location = st.text_input("Enter End Location")

network_provider = st.selectbox(
    "Select Network Service Provider",
    ["Airtel", "Jio", "Vi", "BSNL"]
)

# Function to make an API call
import random
if st.button("Submit"):
    if start_location and end_location:
        # result = call_api(start_location, end_location, network_provider)
        responses = [
            "Use Cash!",
            "Can rely on Digital Payments!",
            "Digital payments are widely accepted, but due to poor network signals of your carrier, use cash.",
            "Digital payments should be fine, but keep some cash handy just in case."
        ]
        response = random.choice(responses)
        st.write("Suggestion:", response)
    else:
        st.error("Please enter both Start and End locations.")
