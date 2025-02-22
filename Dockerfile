# © KronoS
# https://t.me/fakekronos

FROM ubuntu:latest

ENV DEBIAN_FRONTEND=noninteractive

RUN mkdir /Song_Downloader
WORKDIR /Song_Downloader

COPY . ./

RUN apt-get update && apt-get upgrade -y
RUN apt-get install python3-pip -y
RUN apt-get install ffmpeg -y
RUN pip3 install -r requirements.txt

CMD ["python3", "bot.py"]
