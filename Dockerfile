FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY model.pkl model.pkl
COPY score.py score.py

EXPOSE 5000

CMD ["python", "score.py"]
