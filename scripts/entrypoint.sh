#!/bin/bash

set -e

# Realizar as migrações do banco de dados
python manage.py migrate --no-input
echo "COLETANDO ARQUIVOS ESTATICOS"

# Coletar os arquivos estáticos
python manage.py collectstatic --no-input
echo "APLICANDO MIGRACOES"

# Iniciar o servidor uWSGI
uwsgi --http :8000 --module app.wsgi --workers 4 --master --static-map /static=/flix-api/static/
echo "SERVIDOR INICIADO"