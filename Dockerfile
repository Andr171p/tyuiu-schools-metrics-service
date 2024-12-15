FROM python:3.11

WORKDIR /fastapi_service

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8080

CMD ["uvicorn", "src.api_v1.app:app", "--host", "0.0.0.0", "--port", "8000"]