docker stop chat-mysql-prod chat-api-prod
docker rm chat-mysql-prod chat-api-prod
docker rmi -f `docker images chat-concierge_chat-mysql-prod`
docker rmi -f `docker images chat-concierge_chat-api-prod`
sudo docker-compose -f docker-compose.production.yml up -d 