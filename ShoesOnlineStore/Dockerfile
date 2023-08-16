FROM python:3.11.4
LABEL Maintainer="r.nikookolah@gmail.com"
LABEL Owner="RaziyeNikookolah"
LABEL version="v1.1"

# set work directory 
WORKDIR /app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -U pip
RUN pip install -r requirements.txt
COPY . .
EXPOSE 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
