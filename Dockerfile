# Use a imagem base do Python
FROM python:3.11-slim

# Defina o diretório de trabalho
WORKDIR /app

# Copie os arquivos de requisitos e instale as dependências
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copie o restante dos arquivos do projeto
COPY . .

# Exponha a porta em que o Streamlit vai rodar
EXPOSE 8501

# Defina o comando para iniciar o Streamlit
CMD ["streamlit", "run", "app.py"]
