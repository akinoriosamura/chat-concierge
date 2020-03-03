docker stop `docker ps -qa`
docker rm `docker ps -qa`
docker rmi -f `docker images chat-concierge_uwsgi`
docker rmi -f `docker images chat-concierge_nginx`
docker-compose up -d
