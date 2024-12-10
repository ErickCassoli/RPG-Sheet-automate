# Base com a última versão do Python
FROM mcr.microsoft.com/devcontainers/python:1.1-3.12-bullseye

# Configurar diretório de trabalho
WORKDIR /workspace

# Instalar dependências do sistema (se necessário para pacotes como numpy)
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Atualizar pip
RUN pip install --no-cache-dir --upgrade pip

# Instalar Poetry (futuro uso)
RUN pip install poetry

# Configurar como pasta inicial
CMD [ "bash" ]
