FROM python:3.12-slim

ENV DEBIAN_FRONTEND noninteractive

RUN apt-get update && apt-get install -yqq socat
WORKDIR /home/user/

COPY ./server.py /home/user/server.py

CMD ["socat", "TCP-L:53117,fork,reuseaddr", "EXEC:'python server.py'"]
