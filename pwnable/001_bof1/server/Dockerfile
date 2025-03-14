FROM ubuntu:22.04@sha256:7a57c69fe1e9d5b97c5fe649849e79f2cfc3bf11d10bbd5218b4eb61716aebe6

ENV LC_CTYPE=C.UTF-8

ENV user prob
ENV chall_port 9999

RUN apt-get update
RUN apt-get -y install socat

RUN useradd -d /home/$user $user -s /bin/bash

WORKDIR /home/$user

ADD $user /home/$user/$user
ADD flag /home/$user/flag

RUN chown -R root:root /home/$user
RUN chown root:$user /home/$user/flag
RUN chown root:$user /home/$user/$user

RUN chmod 755 /home/$user/$user
RUN chmod 440 /home/$user/flag



USER $user
EXPOSE $chall_port
CMD socat TCP-LISTEN:$chall_port,reuseaddr,fork EXEC:/home/$user/$user