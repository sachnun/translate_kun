# install python 3.8.16-slim-bullseye
FROM python:3.8.16-slim-bullseye

# install ffmpeg
RUN apt-get -y update && apt-get -y upgrade && apt-get install -y --no-install-recommends ffmpeg

# set working directory
WORKDIR /usr/src/app

# install dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

# copy project
COPY . .

# run server as uvicorn, port 8000, host 0.0.0.0
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]

# external port
EXPOSE 8000