# app.py
import streamlit as st
import pandas as pd
from src.model import load_model, predict

# Carregar o modelo
model = load_model('/app/models/model.pkl')

st.title('Previsão de Ações da AAPL')

uploaded_file = st.file_uploader("Escolha um arquivo CSV", type="csv")
if uploaded_file is not None:
    data = pd.read_csv(uploaded_file)
    predictions = predict(model, data)
    st.write(predictions)


