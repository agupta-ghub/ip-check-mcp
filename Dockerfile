FROM python:3.11-slim

WORKDIR /app

COPY . /app
RUN pip install fastapi uvicorn requests

ENV PORT=10000

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "10000"]
