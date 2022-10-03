# start rabbitmq server
echo "Starting RabbitMQ Server"
docker run -it --rm --name rabbitmq -p 5672:5672 -p 15672:15672 rabbitmq:3.10-management
echo "RabbitMQ Server Ended"