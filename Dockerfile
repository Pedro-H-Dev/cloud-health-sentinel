# Usa uma imagem oficial leve do Python
FROM python:3.11-slim

# Define a pasta de trabalho dentro do container
WORKDIR /app

# Copia o arquivo de dependências e instala as bibliotecas
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copia o script Python para dentro do container
COPY main.py .

# Comando que será executado quando o container ligar
CMD ["python", "main.py"]