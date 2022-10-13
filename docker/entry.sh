#!/bin/bash

# start in server mode if no command is specified
if [ $# -eq 0 ]; then
    echo "Starting in server mode"
    pypokergui serve /src/config/conf.yaml --port 8000
    exit 0
fi

# start in cli mode 
if [ $1 = 'cli' ]; then
    echo "Starting in cli mode"
    pypokergui cli /src/config/conf.yaml -r 1 -v 2
    exit 0
fi

# start in server mode
if [ $1 = 'server' ]; then
    echo "Starting in server mode"
    pypokergui serve /src/config/conf.yaml --port 8000
    exit 0
fi