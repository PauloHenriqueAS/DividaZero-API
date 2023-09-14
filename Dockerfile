# Use a imagem base Python
FROM python:3.9

# Defina o diretório de trabalho no contêiner
WORKDIR /app

# Copie os requisitos para o diretório de trabalho
COPY requirements.txt .

# Instale as dependências
RUN pip install -r requirements.txt

# Copie todo o código fonte para o diretório de trabalho
COPY . .

# Exponha a porta que o FastAPI irá usar (substitua a porta pelo que você estiver usando)
EXPOSE 8000

# Comando para iniciar o aplicativo FastAPI
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
