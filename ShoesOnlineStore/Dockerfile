FROM python:3.11.4-alpine



RUN mkdir /e-commerce

# set work directory
WORKDIR /e-commerce

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt /requirements.txt
RUN pip install -r /requirements.txt