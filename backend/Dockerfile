FROM python:3.10.2-slim

RUN apt update && apt install -y --no-install-recommends \ 
    default-jre \
    git \
    zsh \
    curl \
    wget \
    unzip

RUN wget https://download.jetbrains.com/fonts/JetBrainsMono-1.0.0.zip && \
    unzip JetBrainsMono-1.0.0.zip && \
    mv JetBrainsMono-*.ttf /usr/share/fonts/

RUN useradd -ms /bin/bash python

USER python

WORKDIR /home/python/app

ENV PYTHONPATH=${PYTHONPATH}/home/python/app/src
ENV JAVA_HOME=/usr/lib/jvm/java-11-openjdk-amd64

RUN sh -c "$(wget -O- https://github.com/deluan/zsh-in-docker/releases/download/v1.1.5/zsh-in-docker.sh)" -- \
    -t https://github.com/denysdovhan/spaceship-prompt \
    -p git \
    -p https://github.com/zsh-users/zsh-autosuggestions \
    -p https://github.com/zsh-users/zsh-completions \
    -p https://github.com/zsh-users/zsh-syntax-highlighting \
    -a 'SPACESHIP_USER_SHOW=always' \
    -a 'SPACESHIP_PROMPT_ADD_NEWLINE=true' \
    -a 'ENABLE_CORRECTION="true"' \
    -a 'CASE_SENSITIVE="true"' \
    -a 'alias py="python3"'

CMD [ "tail", "-f", "/dev/null" ]
