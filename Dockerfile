FROM python:3.8-slim-buster

WORKDIR /app

# تثبيت أدوات أساسية للبناء
RUN apt-get update && apt-get install -y gcc libffi-dev libssl-dev

COPY requirements.txt requirements.txt
RUN pip3 install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python3", "IEX.py"]
