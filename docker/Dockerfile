# Use uma imagem oficial Python leve
FROM python:3.11-slim

# Define o diretório de trabalho dentro do container
WORKDIR /app

# Copia os arquivos de dependências e instala
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# Copia todo o código para dentro do container
COPY . .

# Exponha a porta onde o Flask irá rodar
EXPOSE 5002

# Comando para iniciar a aplicação
CMD ["python", "app.py"]
