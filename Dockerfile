FROM python:3.8

ENV PYTHONUNDUFFERED 1

WORKDIR /house_rest

COPY requirements.txt ./
RUN pip3 install -r requirements.txt

COPY . /house/