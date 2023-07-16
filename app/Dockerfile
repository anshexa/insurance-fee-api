FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY ../requirements.txt /tmp/requirements.txt
RUN pip --no-cache-dir install --upgrade pip & \
    pip install -r /tmp/requirements.txt

WORKDIR /src/app

COPY . /src/app/