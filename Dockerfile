FROM python:3.7-alpine

ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

RUN mkdir /profiles_project
WORKDIR /profiles_project
COPY ./profiles_project/ /profiles_project

RUN adduser -D user
USER user