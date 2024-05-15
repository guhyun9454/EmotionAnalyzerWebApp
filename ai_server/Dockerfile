FROM python:3.11.4

WORKDIR /app

COPY requirements.txt .

RUN apt-get update && apt-get install -y \
    libgl1-mesa-glx
    
RUN pip install -r requirements.txt

COPY . .

EXPOSE 9454

ENTRYPOINT ["python", "server.py"]
