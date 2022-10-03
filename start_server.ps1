# start Poker server
echo "Starting Poker Server"

# remove image if found
if($(docker images -q poker_server)){
    echo "Removing poker_server image"
    docker rmi poker_server -f
}

# build image
echo "Building poker_server image"
docker build -t poker_server .
# run container
echo "Running server container"
docker run -it --rm --name=poker_server_test -p 80:8000 poker_server
echo "Poker server Ended"