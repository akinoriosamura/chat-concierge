docker stop chat-mysql-dev
docker rm chat-mysql-dev
docker rmi -f `docker images chat-concierge_chat-mysql-dev`
sudo docker-compose -f docker-compose.development.yml up -d 
