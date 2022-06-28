# syntax=docker/dockerfile:1
FROM python:3.7-alpine
WORKDIR /code
ENV FLASK_APP=Controller/main_scores.py
ENV FLASK_RUN_HOST=0.0.0.0
COPY requirements.txt requirements.txt
COPY Utills/score.py
RUN pip install -r requirements.txt
EXPOSE 5000
COPY . .
CMD ["flask", "run"]