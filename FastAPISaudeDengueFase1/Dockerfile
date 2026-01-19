FROM ubuntu:latest
LABEL authors="Rodrigo Oliveira de Andrade"

# Imagem base do Python
FROM python:3.12

# Diretório de trabalho dentro do container
WORKDIR /app

# Copiar arquivos do projeto para dentro do container
COPY . /app

# Instalar dependências
RUN pip install --no-cache-dir -r requirements.txt

# Expor a porta que a API vai usar
EXPOSE 8001

# Comando para iniciar a aplicação
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8001"]
