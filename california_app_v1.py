import streamlit as st
st.title("California Housing Application")

MedInc = st.number_input("Median Income")
HouseAge = st.number_input("House Age")
AveRooms = st.number_input("Average Rooms")
AveBedrms = st.number_input("Average Bedrooms")
Population = st.number_input("Population")
AveOccup = st.number_input("Average Occupancy")
Latitude = st.number_input("Latitude")
Longitude = st.number_input("Longitude")

import joblib
loaded_model = joblib.load("california.joblib")
prediction = loaded_model['model'].predict([[MedInc, HouseAge, AveRooms, AveBedrms, Population, AveOccup, Latitude, Longitude]])

if st.button("Predict"):
    st.write(f"Predicted House Value: {round(prediction[0],2)}")