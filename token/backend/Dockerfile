FROM tiangolo/uvicorn-gunicorn-fastapi:python3.11

COPY . /app

RUN pip install --no-cache-dir -r requirements.txt

CMD ["uvicorn", "main:app", "--reload", "--host", "0.0.0.0", "--port", "8000"]