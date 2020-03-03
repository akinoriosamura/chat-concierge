# chat-concierge

## setup
 - clone
 - set `.env` in `chat-concierge/`
 ``` 
 .env has
 GooglePlaceAPI
 YOUR_CHANNEL_ACCESS_TOKEN
 YOUR_CHANNEL_SECRET
 ```
 - set `build` of react-setting in `chat-concierge/`

## develop run
### build
```
docker-compose up -d
 - flask run も走る
```

### check link
 - please check url and api key of .env  

### db create if not
```
docker exec -it chat-api /bin/bash
cd chat
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

### api shell
```
docker attach  chat-api
```

### attach mysql
pass: in `docker-compose.yml`
```
docker-compose exec chat-mysql mysql -u root -p
```

### test
```
docker exec -it chat-api /bin/bash
cd chat
pipenv run test
Ctrl + c
```

## api ref
 - callback & LIFF  
(line official account manager)[https://manager.line.biz/]  
 - LIFF app link
 https://developers.line.biz/console/channel/1626501382
 - rich menu  
(line developer)[https://developers.line.biz/console/channel/1626501382/basic/]  
 - inquiry
https://docs.google.com/forms/d/1mQqv4M-cW4jXUc0JOQvZ-2saVRPczxSD57-CR4NyN-4/edit

## connect to line api
 - change Endpoint URL in line dev for LIFF  
 https://developers.line.biz/console/channel/1626501382/liff/1626501382-xMvalEMJ  
 - change Webhook URL  in line dev for message API  
 https://developers.line.biz/console/channel/1626501382/messaging-api
 - run rich menu  
 https://manager.line.biz/account/@968puzvz/richmenu/2092848

## until release production server
 - flask, gunicorn(wsgi), nginx(web server), docker
https://testdriven.io/courses/tdd-flask/deployment/
https://qiita.com/arata-honda/items/e22c9df83df8ee0e9c4c
http://docs.docker.jp/compose/production.html
https://www.slideshare.net/zaruhiroyukisakuraba/railsdocker-78973487
https://github.com/CircleCI-Public/circleci-demo-docker/blob/master/.circleci/config.yml

