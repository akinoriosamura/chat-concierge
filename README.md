# chat-concierge

## api ref
(line developer)[https://developers.line.biz/console/channel/1626501382/basic/]  
 - callback & LIFF  
(line official account manager)[https://manager.line.biz/]  
 - rich menu  

## run
### build
```
docker-compose up -d
 - flask run も走る
```

### check link
 - please check url and api key

### db create if not
```
docker exec -it chat-api /bin/bash
cd chat
flask db init
flask db migrate
flask db upgrade
Ctrl + c
```

### ngrok
 - install ngrok
 - run ngrok
 ```
 ngrok htttps 4000
 ```

### in line
 - open AI コンシェルジュ
 - tap rich menu

## api shell
```
docker attach  chat-api
```

## attach mysql
```
docker-compose exec chat-mysql mysql -u root -p
```

## test
```
docker exec -it chat-api /bin/bash
cd chat
pipenv run test
Ctrl + c
```