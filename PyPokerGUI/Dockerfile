FROM python:3.5
COPY . /src/pypokergui
RUN pip install -e /src/pypokergui -i https://pypi.tuna.tsinghua.edu.cn/simple
EXPOSE 8000/tcp
STOPSIGNAL SIGTERM
ENTRYPOINT ["pypokergui", "serve", "/app/conf.yaml", "--port", "8000"]

# docker run -it --rm --name=poker_gui_test -v $(pwd)/example:/app -p 8888:8000 poker_gui
