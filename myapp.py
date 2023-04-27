import streamlit as st
import pandas as pd

st.title("Ma première application Streamlit")

st.write("Bienvenue dans cette application! Voici un exemple d'image:")
age = st.slider('Quel est votre âge?', 0, 100, 25)
st.write("Vous avez", age, "ans")


