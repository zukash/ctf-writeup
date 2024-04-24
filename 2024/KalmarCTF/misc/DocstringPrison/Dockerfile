FROM python:3.11.3@sha256:3a619e3c96fd4c5fc5e1998fd4dcb1f1403eb90c4c6409c70d7e80b9468df7df
# Hmmm, that's not the latest version of python!

RUN apt-get update && apt-get -y install socat

RUN useradd -u 1000 -m -s /bin/bash user
WORKDIR /home/user

COPY code_to_comment.py .
COPY server.py .
COPY flag.py .
# COPY . .

RUN chown -R user:user /home/user
USER user:user

CMD export PYTHONDONTWRITEBYTECODE=1; socat -T 240 TCP-L:8532,fork,reuseaddr EXEC:"python3 server.py"

