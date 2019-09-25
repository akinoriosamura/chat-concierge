FROM python:3.7

RUN apt-get update

COPY . /app
WORKDIR /app

# install pipenv
RUN pip install -U pip && \
    pip install pipenv && \
    pipenv install --dev --system