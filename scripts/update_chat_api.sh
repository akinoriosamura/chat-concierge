docker stop chat-api-prod
docker rm chat-api-prod
docker rmi -f `docker images chat-concierge_chat-api-prod`
sudo docker-compose -f docker-compose.production.yml up -d 