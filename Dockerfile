# install python latest version
FROM python:latest

# install ffmpeg
RUN apt-get -y update && apt-get -y upgrade && apt-get install -y --no-install-recommends ffmpeg

# set working directory
WORKDIR /usr/src/app

# set environment variables
COPY requirements.txt requirements.txt

# install dependencies
RUN pip3 install -r requirements.txt

# copy project
COPY . .

# run server
CMD [ "python3", "./main.py" ]

# external port
EXPOSE 8000