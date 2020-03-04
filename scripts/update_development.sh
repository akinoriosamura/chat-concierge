docker stop chat-api-dev
docker rm chat-api-dev
docker rmi -f `docker images chat-concierge_chat-api-dev`
docker-compose -f docker-compose.development.yml up -d 
