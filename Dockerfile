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

# run server as uvicorn, port 8000, host 0.0.0.0, and workers 2
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--workers", "2"]

# external port
EXPOSE 8000