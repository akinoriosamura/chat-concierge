docker stop chat-ssl-prod
docker rm chat-ssl-prod
docker rmi -f `docker images steveltn/https-portal`
sudo docker-compose -f docker-compose.production.yml up -d
