FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt ./

RUN apt update
RUN pip install --upgrade pip

RUN pip install --no-cache-dir -r requirements.txt


COPY . .

CMD ["bash", "/app/scripts/entrypoint.sh"]
