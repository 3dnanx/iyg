FROM python:3.8-slim-buster

WORKDIR /app

# تثبيت الأدوات والمكتبات الأساسية اللي بعض الباكيجات تحتاجها
RUN apt-get update && apt-get install -y \
    gcc \
    libffi-dev \
    libssl-dev \
    make \
    && rm -rf /var/lib/apt/lists/*

# تثبيت المتطلبات
COPY requirements.txt requirements.txt
RUN pip3 install --no-cache-dir -r requirements.txt

# نسخ باقي الملفات
COPY . .

# تشغيل البوت
CMD ["python3", "IEX.py"]
