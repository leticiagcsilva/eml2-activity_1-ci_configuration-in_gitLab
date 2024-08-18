import streamlit as st
import pandas as pd
from model import predict, load_model

# Carregar o modelo
model = load_model('model/model.pkl')

st.title('Previsão de Ações AAPL')

uploaded_file = st.file_uploader("Escolha um arquivo CSV", type="csv")
if uploaded_file:
    data = pd.read_csv(uploaded_file)
    st.write(data)
    
    # Fazer previsões
    predictions = predict(model, data)
    st.write("Previsões:")
    st.write(predictions)


