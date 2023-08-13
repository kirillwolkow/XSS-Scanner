FROM python:3.9.5-slim-buster

# set environment variables  
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# create the app user
RUN adduser --system --group django_user

# set work directory
WORKDIR /usr/src/app

# install system packages required by Wagtail and Django.
RUN apt-get update --yes --quiet && apt-get install --yes --quiet --no-install-recommends \
    nano \
    build-essential \
    gettext \
    libpq-dev \
    libjpeg62-turbo-dev \
    zlib1g-dev \
    libwebp-dev \
    python3-dev \
    libpq-dev \ 
    gcc \
    musl-dev \
    && rm -rf /var/lib/apt/lists/*

# install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt

# copy project
COPY ./django_xss_scanner .

# chown all the files to the app user
RUN chown -R django_user:django_user /usr/src/app

# change to the app user
USER django_user