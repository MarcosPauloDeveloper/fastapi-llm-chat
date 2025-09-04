FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /app

# dependencies
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# code
COPY app ./app

# port
ENV PORT=8000

# start
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
