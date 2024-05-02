FROM python:3.11.4

WORKDIR /app

COPY . .

RUN apt-get update && apt-get install -y \
    libgl1-mesa-glx
    
RUN pip install -r requirements.txt

EXPOSE 9454

CMD ["python", "server.py"]
