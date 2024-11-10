# Use uma imagem oficial do Python como base
FROM python:3.12-alpine3.18

ENV PYTHONDONTWRITEBYTECODE 1

ENV PYTHONUNBUFFERED 1

# Copie o código do projeto para o contêiner
COPY ./network /network  
COPY ./scripts /scripts

# Defina o diretório de trabalho no contêiner
WORKDIR /network

# Copie o arquivo de dependências do projeto para o contêiner
COPY ./network/requirements.txt .

# Instale as dependências do projeto
RUN pip install --no-cache-dir -r requirements.txt


# Exponha a porta onde o Django vai rodar
EXPOSE 8000


RUN adduser --disabled-password --no-create-home duser && \
  mkdir -p /data/web/static && \
  mkdir -p /data/web/media && \
  chown -R duser:duser /data/web/static && \
  chown -R duser:duser /data/web/media && \
  chmod -R 755 /data/web/static && \
  chmod -R 755 /data/web/media && \
  chmod -R +x /scripts



CMD ["/scripts/commands.sh"]
