FROM python:3.8-slim-buster

# install ffmpeg
# RUN apt-get update && apt-get install -y ffmpeg

WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip3 install -r requirements.txt

COPY . .

CMD [ "python3", "-m" , "uvicorn", "main:app", "--host=0.0.0.0"]

# external port
EXPOSE 8000