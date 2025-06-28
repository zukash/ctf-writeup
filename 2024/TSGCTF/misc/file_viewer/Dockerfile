FROM ubuntu:24.04

RUN apt update && \
        apt -y upgrade && \
        apt install -y xinetd iproute2 libc++1
RUN groupadd -r user && useradd -r -g user user

COPY --chown=root:user ./build/ctf.conf /etc/xinetd.d/ctf
COPY --chown=root:user ./build/files /home/user
COPY --chown=root:user ./build/start.sh /home/user/start.sh
COPY --chown=root:user ./dist/chal /home/user/chal

WORKDIR /home/user

RUN chown -R root:user /home/user

USER user

CMD ["xinetd","-dontfork","-f","/etc/xinetd.d/ctf"]
