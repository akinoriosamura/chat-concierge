# chat-concierge

## build
```
docker-compose up -d
```

## start
```
docker exec -it chat-api /bin/bash
cd chat
flask db init
flask db migrate
flask db upgrade
Ctrl + c
```

## attach mysql
```
docker-compose exec chat-mysql mysql -u root -p
```

## test
```
docker exec -it chat-api /bin/bash
pipenv run test
Ctrl + c
```