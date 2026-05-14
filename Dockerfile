FROM python:3.12-slim

COPY init.sql /docker-entrypoint-initdb.d/

WORKDIR /app

COPY ./app/requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY ./app .

RUN chmod +x ./script.sh

EXPOSE 5000

CMD ["script.sh"]

