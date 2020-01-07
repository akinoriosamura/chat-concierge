# chat-concierge

## api ref
 - callback & LIFF  
(line official account manager)[https://manager.line.biz/]  
 - LIFF app link
 https://developers.line.biz/console/channel/1626501382
 - rich menu  
(line developer)[https://developers.line.biz/console/channel/1626501382/basic/]  
 - inquiry
https://docs.google.com/forms/d/1mQqv4M-cW4jXUc0JOQvZ-2saVRPczxSD57-CR4NyN-4/edit


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
 ngrok htttp 3031
 ```
 - change ngork link in line developer  
 https://developers.line.biz/console/channel/1626501382/liff/1626501382-xMvalEMJ  

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