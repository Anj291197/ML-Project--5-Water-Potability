import pickle
import streamlit as st
import sklearn


df = pickle.load(open("water_model.pkl","rb"))

st.title("Water Potability Prediction using ML")

ph = st.text_input("Enter the ph level")
Hardness = st.text_input("Enter the Hardness level")
Solids= st.text_input("Enter the amount of Solids")
Chloramines = st.text_input("Enter the amount of Chloramines")
Sulfate = st.text_input("Enter the amount of Sulfate")
Conductivity = st.text_input("Conductivity level of water")
Organic_carbon = st.text_input("Enter the amount of Organic Carbon")
Trihalomethanes = st.text_input("Enter the amount of Trihalomethanes")
Turbidity = st.text_input("Enter the Turbidity")

dia_water = ""

#Creating button for prediction
if st.button("Predict"):
    dia_water_pred = df.predict([[ph, Hardness, Solids,Chloramines,Sulfate,Conductivity,Organic_carbon,Trihalomethanes,Turbidity]])

    if dia_water_pred[0] == 1:
        dia_water = "Water is Potable"
    else:
        dia_water = "Water is not Potable"
st.success(dia_water)