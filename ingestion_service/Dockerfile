FROM python:3.11-slim

WORKDIR app


COPY ingestion_service/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY ingestion_service ./ingestion_service
COPY base_images ./base_images



CMD ["python","./ingestion_service/main.py"]