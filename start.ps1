# start RabbitMQ if needed
if(!$(docker ps -q -f name=rabbitmq)){
    Write-Output "Starting RabbitMQ Server"
    docker run -d -it --rm --name rabbitmq -p 5672:5672 -p 15672:15672 rabbitmq:3.10-management
}

# stop old server
if($(docker ps -q -f name=poker_server_test)){
    Write-Output "Stopping old conatiner"
    docker stop poker_server_test
}

# start Poker server
Write-Output "Starting Poker Server"

# remove image if found
if($(docker images -q poker_server)){
    Write-Output "Removing poker_server image"
    docker rmi poker_server -f
}

# build image
Write-Output "Building poker_server image"
docker build -t poker_server .

# if argument server is passed, start server
if($args[0] -eq "server"){
    Write-Output "Starting container in server mode"
    docker run -d -it --rm --name=poker_server_test -p 80:8000 poker_server server
}
# else if argument cli is passed, start cli
elseif($args[0] -eq "cli"){
    Write-Output "Starting container in cli mode"
    docker run -it --rm --name=poker_server_test -p 80:8000 poker_server cli
}
# else if argument is passed, pass it to docker
elseif($args[0]){
    Write-Output "Starting container"
    docker run -d -it --rm --name=poker_server_test -p 80:8000 poker_server $args[0]
}
else{
    Write-Output "Starting container in server mode"
    docker run -d -it --rm --name=poker_server_test -p 80:8000 poker_server
}
