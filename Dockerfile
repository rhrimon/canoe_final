#select base image to use
FROM python:3.8.9-slim-buster

RUN apt-get update 
RUN apt-get install -y wget gconf-service libasound2 libatk1.0-0 libcairo2 libcups2 libfontconfig1 libgdk-pixbuf2.0-0 libgtk-3-0 libnspr4 libpango-1.0-0 libxss1 fonts-liberation libappindicator1 libnss3 lsb-release xdg-utils

#download and install chrome
RUN wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
RUN dpkg -i google-chrome-stable_current_amd64.deb; apt-get -fy install

#install python dependencies
COPY requirements.txt requirements.txt 
RUN pip install -r ./requirements.txt 

#set environment port
ENV PORT 5000

#set workspace
WORKDIR /canoe_final/final_tests
COPY . /canoe_final/final_tests

#keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE=1

#turns off buffering for easier container logging
ENV PYTHONUNBUFFERED=0

CMD ["pytest", "-vv"]