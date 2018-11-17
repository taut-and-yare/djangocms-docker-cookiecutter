FROM python:3.6

RUN apt-get -qq update && apt-get install -y jpegoptim optipng

ADD . /project
WORKDIR /project

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

RUN chmod +x /project/bin/uwsgi.sh
