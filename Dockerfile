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
COPY ./Pokershark /src/Pokershark

# configure server
EXPOSE 8000/tcp
STOPSIGNAL SIGTERM

# entry point
#ENTRYPOINT ["pypokergui", "serve", "/src/Pokershark/conf.yaml", "--port", "8000"]
# pypokergui serve /src/Pokershark/conf.yaml --port 8000
ENTRYPOINT ["/bin/bash"]