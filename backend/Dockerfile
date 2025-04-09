FROM python:3.12.4

WORKDIR /app

COPY requirements.txt .
RUN pip install --upgrade pip 
RUN pip install --no-cache-dir -r requirements.txt --retries 10 --timeout 60

COPY . /app/
COPY ./wait-for-it.sh /app/

RUN chmod +x /app/wait-for-it.sh
RUN chmod 644 /app/.env

CMD ["python", "src/manage.py", "runserver", "0.0.0.0:8000"]
