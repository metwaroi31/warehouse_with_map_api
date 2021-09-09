# Base Image
FROM python:3.6

# set default environment variables
# ENV PYTHONUNBUFFERED 1
# ENV LANG C.UTF-8
# ENV DEBIAN_FRONTEND=noninteractive 

WORKDIR /app

# Install project dependencies
COPY ./requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

# Add current directory code to working directory
COPY . /app

CMD python3 main.py