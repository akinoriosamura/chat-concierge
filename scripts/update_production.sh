docker stop chat-api-prod chat-nginx-prod chat-ssl-prod
docker rm chat-api-prod chat-nginx-prod chat-ssl-prod
docker rmi -f `docker images chat-concierge_chat-api-prod`
docker rmi -f `docker images chat-concierge_chat-nginx-prod`
docker rmi -f `docker images steveltn/https-portal`
sudo docker-compose -f docker-compose.production.yml build
sudo docker-compose -f docker-compose.production.yml up -d 
