FROM python:3.5

# update packages
RUN apt update

# install tools
RUN apt install -y nano

# install python packages
RUN pip install pika

# setup poker engine
COPY ./PyPokerEngine /src/pypokerengine
RUN pip install -e /src/pypokerengine


# setup server
COPY ./PyPokerGUI /src/pypokergui
RUN pip install -e /src/pypokergui

# setup players
COPY ./Config /src/config

# configure server
EXPOSE 8000/tcp

# entry point
COPY ./docker /src/docker
Run chmod +x /src/docker/entry.sh
# fix stupid line endings bug
RUN sed -i -e 's/\r$//' /src/docker/entry.sh
ENTRYPOINT ["./src/docker/entry.sh"]