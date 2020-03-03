docker stop chat-api
docker rm chat-api
docker rmi -f `docker images chat-concierge_chat-api`
sudo docker-compose up -d
echo `update chat docker`
