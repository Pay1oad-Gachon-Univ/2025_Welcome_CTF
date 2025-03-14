FROM ubuntu:22.04@sha256:77906da86b60585ce12215807090eb327e7386c8fafb5402369e421f44eff17e

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
