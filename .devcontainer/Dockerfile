FROM python:3.11-trixie

# define o app como diretório de trabalho
WORKDIR /app

# copia os requisitos
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# copia o restante do código
COPY . .

# executa o servidor apontando para a pasta correta
CMD ["python", "api/manage.py", "runserver", "0.0.0.0:8000"]