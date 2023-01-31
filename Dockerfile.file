FROM python:3.8-slim-buster
MAINTAINER CTRL-META SOFT.

ENV PYTHONUNBUFFERED=1

RUN mkdir /opt/lemon-app
WORKDIR /opt/lemon-app
COPY requirements.txt .
RUN pip3 install -r requirements.txt
COPY . .
#CMD ["python3","manage.py","runserver"]
