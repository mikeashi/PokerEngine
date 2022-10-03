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
#RUN pip install -e /src/pypokerengine -i https://pypi.tuna.tsinghua.edu.cn/simple


# setup server
COPY ./PyPokerGUI /src/pypokergui
RUN pip install -e /src/pypokergui
#RUN pip install -e /src/pypokergui -i https://pypi.tuna.tsinghua.edu.cn/simple

# setup players
COPY ./Config /src/config

# configure server
EXPOSE 8000/tcp
STOPSIGNAL SIGTERM

# entry point
#ENTRYPOINT ["pypokergui", "serve", "/src/config/conf.yaml", "--port", "8000"]
ENTRYPOINT ["/bin/bash"]