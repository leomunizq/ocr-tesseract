
FROM python:3.11-slim


RUN apt-get update && apt-get install -y \
    tesseract-ocr \
    tesseract-ocr-ita \
    && rm -rf /var/lib/apt/lists/*


WORKDIR /app


COPY infrastructure/requirements.txt .  
RUN pip install --no-cache-dir -r requirements.txt


COPY app /app


EXPOSE 8500


CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8500", "--reload"]
