docker stop chat-api-prod chat-nginx-prod
docker rm chat-api-prod chat-nginx-prod
docker rmi -f `docker images chat-concierge_chat-api-prod`
docker rmi -f `docker images chat-concierge_nginx-prod`
docker-compose -f docker-compose.production.yml up -d 
