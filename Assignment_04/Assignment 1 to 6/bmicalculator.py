import streamlit as st

st.title("BMI Calculator")

weight = st.slider("Set the weight in KG: ", 50,200, 100)
height = st.slider("Set the height in cm: ", 100, 250, 150)

bmi = weight / (height/100)**2


st.success(f"The BMi is {bmi:.2f}")



