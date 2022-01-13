FROM python:3.9

ENV PYTHONUNDUFFERED 1

WORKDIR /urs/src/house_rest

COPY requirements.txt ./
RUN pip3 install -r requirements.txt

COPY . /urs/src/house_rest/