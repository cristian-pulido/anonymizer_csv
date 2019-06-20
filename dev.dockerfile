# Image based on the official Python 3 image from dockerhub
FROM python:3.7.3

# Change directory so that commands run inside this new directory
WORKDIR /app

# Python install
COPY requirements.txt ./
RUN pip install -r requirements.txt

# Code
COPY . ./

# Download model in spanish
RUN python -m spacy download es_core_news_sm

# Grant execution permission
RUN chmod 700 ./scrubber.19.0403L/scrubber.19.0403.lnx
