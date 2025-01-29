# 📝 OCR API with FastAPI and Tesseract

This project is a **FastAPI-based OCR (Optical Character Recognition) API** that uses **Tesseract-OCR** to extract text from images. The API is containerized with **Docker**, deployed using **Portainer**, and the image is stored in **AWS ECR**.

---

## 🚀 Features

- ✅ **FastAPI** framework for high-performance API.
- ✅ **Tesseract-OCR** for optical character recognition.
- ✅ **Pre-processing techniques** (grayscale, contrast adjustment, binarization).
- ✅ **Dockerized application** for easy deployment.
- ✅ **AWS ECR** for container storage.
- ✅ **Portainer compatibility** for easy management.
- ✅ **Optimized Tesseract settings** (`--oem 1 --psm 3 -l ita`).

---

## 🏗️ Project Structure

📦 ocr-tesseract
┣ 📂 app
┃┣ 📜 main.py # FastAPI application
┃┗ 📜 ocr.py # OCR processing logic
┣ 📂 infrastructure
┃ ┣ 📜 Dockerfile # Docker setup
┃ ┣ 📜 docker-compose.yml # Container configuration
┃ ┗ 📜 requirements.txt # Python dependencies
┗ 📜 README.md

---

## 🔧 Installation & Setup

### **1️⃣ Clone the repository**

### _2️⃣ Set up a virtual environment (optional)_

```bash python3 -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
pip install -r infrastructure/requirements.txt
```

### **_3️⃣ Run the API Locally with Docker Compose_**

Instead of running manually, use Docker Compose:

```bash
cd infrastructure
docker-compose up --build -d
```

This will:

Build the Docker image
Start the container in detached mode (-d)
Expose the API on port 8500
