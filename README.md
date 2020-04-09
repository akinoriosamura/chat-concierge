# chat-concierge

## setup
 - clone
 - set `.env` in `chat-concierge/`
 ``` 
 .env has
 GooglePlaceAPI
 # LineMessaginAPI
 YOUR_CHANNEL_ACCESS_TOKEN
 YOUR_CHANNEL_SECRET
 ```
 - set `build` of react-setting in `chat-concierge/`

## Development
### build
```
sh scripts/update_development.sh
 - flask run も走る
```

### check link
 - please check url and api key of .env  

### db create if not
```
docker exec -it chat-api-dev /bin/bash
cd server
flask db init
flask db migrate
flask db upgrade
Ctrl + p + q
```

### ngrok
 - install ngrok
 - run ngrok
 ```
 ngrok htttp 3031
 ```

### set ngrok link to messaging api and LIFF
 https://developers.line.biz/console/channel/1626501382

### in line
 - open AI コンシェルジュ
 - tap rich menu

## Production run
### setup
 - set `.env` in `chat-concierge/`
 ``` 
 .env has
 GooglePlaceAPI
 # LineMessaginAPI
 YOUR_CHANNEL_ACCESS_TOKEN
 YOUR_CHANNEL_SECRET
 ```
 - set `build` of react-setting in `chat-concierge/`

### build
```
sh scripts/update_production.sh
```

### check link
 - please check url and api key of .env  

### db upgrade from dev migration
```
docker exec -it chat-api-prod /bin/bash
cd server
flask db upgrade
Ctrl + p + q
```

### set server public link to messaging api and LIFF
 https://developers.line.biz/console/channel/1626501382

### in line
 - open AI コンシェルジュ
 - tap rich menu


## Other

### api shell
```
docker attach  chat-api
```

### attach mysql
pass: in `docker-compose.yml`
```
docker-compose -f docker-compose.development.yml exec chat-mysql-dev mysql -u root -p```

### test
```
docker exec -it chat-api /bin/bash
cd app
pipenv run test
Ctrl + c
```

### api ref
 - callback & LIFF  
(line official account manager)[https://manager.line.biz/]  
 - LIFF app link
 https://developers.line.biz/console/channel/1626501382
 - rich menu  
(line developer)[https://developers.line.biz/console/channel/1626501382/basic/]  
 - inquiry
https://docs.google.com/forms/d/1mQqv4M-cW4jXUc0JOQvZ-2saVRPczxSD57-CR4NyN-4/edit

### connect to line api
 - change Endpoint URL in line dev for LIFF  
 https://developers.line.biz/console/channel/1626501382/liff/1626501382-xMvalEMJ  
 - change Webhook URL  in line dev for message API  
 https://developers.line.biz/console/channel/1626501382/messaging-api
 - run rich menu  
 https://manager.line.biz/account/@968puzvz/richmenu/2092848

