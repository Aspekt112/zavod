FROM ubuntu:16.04

MAINTAINER Nurmatov Artem

RUN mkdir /zavod
COPY . /zavod
WORKDIR /zavod/assets/static

RUN apt-get update
RUN apt-get install -y curl python-pip libpq-dev python-dev
RUN curl -sL https://deb.nodesource.com/setup_8.x | bash
RUN apt-get install -y nodejs
 
RUN npm install -g gulp
RUN npm install
RUN gulp build


WORKDIR /zavod
RUN chmod +x ./entrypoint.sh
RUN pip install -r dependence.txt

EXPOSE 80
CMD python manage.py runserver 0.0.0.0:80
