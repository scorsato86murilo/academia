#!/bin/bash
# Exit on error
set -o errexit

# Modifique conforme seu gerenciador de pacotes (pip, poetry, etc.)
pip install -r requirements.txt

# Coletar arquivos estáticos
python manage.py collectstatic --no-input

# Aplicar migrações pendentes no banco de dados
python manage.py migrate

# Aguardar 1 minuto (60 segundos)
echo "Aguardando 1 minuto..."
sleep 60

# Criar o superusuário (se não existir)
python -c "
from django.contrib.auth.models import User
from django.conf import settings

username = 'adminadmin'
password = '123'
email = 'admin@meudominio.com'

# Verifica se o superusuário já existe
if not User.objects.filter(username=username).exists():
    User.objects.create_superuser(username=username, email=email, password=password)
    print(f'Superusuário {username} criado com sucesso.')
else:
    print(f'Superusuário {username} já existe.')
"

# Iniciar o servidor com Gunicorn + UvicornWorker
python -m gunicorn mysite.asgi:application -k uvicorn.workers.UvicornWorker
