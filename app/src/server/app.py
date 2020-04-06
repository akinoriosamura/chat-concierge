import os
import datetime
import json

from src.recommender import dialogue_manager
import src.server.models
from src.server.models.user import User
from src.server.database import init_db, db

from flask import Flask, abort, request, jsonify, render_template

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    FlexSendMessage, FollowEvent, MessageEvent, TextMessage, TextSendMessage, LocationMessage
)


#  initialize app db migrate
def create_app(test=False):
    app = Flask(
        __name__, static_folder="../build/static", template_folder="../build"
    )
    if test:
        app.config.from_object('src.server.config.TestingConfig')
    else:
        app.config.from_object('src.server.config.Config')
    init_db(app)

    return app


app = create_app()

# LINE Access Token
YOUR_CHANNEL_ACCESS_TOKEN = os.environ["YOUR_CHANNEL_ACCESS_TOKEN"]
# LINE Channel Secret
YOUR_CHANNEL_SECRET = os.environ["YOUR_CHANNEL_SECRET"]

line_bot_api = LineBotApi(YOUR_CHANNEL_ACCESS_TOKEN)
handler = WebhookHandler(YOUR_CHANNEL_SECRET)


@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'callback OK'

# フォローイベントの場合の処理
@handler.add(FollowEvent)
def handle_follow(event):
    print("event: ", event)
    UID = event.source.user_id
    print("UID: ", UID)
    # event = {"replyToken": "fe0ad3806cf84871ad4e365a31f8165f",
    # "source": {"type": "user", "userId": "U9dd63684d2d1be8262ae4ada81e84d13"}, "timestamp": 1581601008508, "type": "follow"}
    # create new user
    user = User(UID)
    db.session.add(user)
    db.session.commit()
    msg = 'User {} created'.format(user.user_id)
    print(msg)
    intro_t = '初めまして！レストランを代わりに決めるコンシェルと言います' + chr(0x100001) + '\n'
    intro_t += 'メニューからおすすめボタンを押してくれれば近くで今やってるオススメのレストランを紹介するよ' + chr(0x100033) + '\n'
    intro_t += '価格帯とカテゴリも設定できるよ！'
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=intro_t)
    )

@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    """
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=event.message.text))
    """
    print(event)
    print("reply token: ", event.reply_token)
    if event.type == "message":
        if (event.message.text == "おすすめ"):
            line_bot_api.reply_message(
                event.reply_token,
                [
                    TextSendMessage(text='近くのおすすめのレストランを紹介するから位置情報を送ってね' + chr(0x10008D)),
                    TextSendMessage(text='line://nv/location'),
                ]
            )
        else:
            line_bot_api.reply_message(
                event.reply_token,
                TextSendMessage(text="おすすめを知りたかったら、おすすめボタンを押してね！"))
    else:
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text="おすすめを知りたかったら、おすすめボタンを押してね！"))

@handler.add(MessageEvent, message=LocationMessage)
def handle_location(event):
    print("reply token: ", event.reply_token)
    lat = event.message.latitude
    lon = event.message.longitude
    print("位置情報", event.message)

    # manager取得
    # manager = dialogue_manager.DialogueManager(35.66, 139.7)
    manager = dialogue_manager.DialogueManager(lat, lon)
    # レコメンド内容取得
    result = manager.gen_recommend_utterance()

    # lineにメッセージ送信 by txt
    line_bot_api.reply_message(
        event.reply_token,
        [
            TextSendMessage(text=result)
        ]
    )

    # lineにメッセージ送信 by fixed
    # import pdb;pdb.set_trace()
    # with open('server/fixed_tmpl_.json') as f:
    #     f_tmpl = json.load(f)
    """
    f_tmpl = {
        "type": "bubble",
        "body": {
            "type": "box",
            "layout": "horizontal",
            "contents": [
            {
                "type": "text",
                "text": "Hello,"
            },
            {
                "type": "text",
                "text": "World!"
            }
            ]
        }
    }
    container_obj = FlexSendMessage.new_from_json_dict(f_tmpl)
    UID = event.source.user_id
    line_bot_api.push_message(UID, messages=container_obj)
    """

@app.route("/")
def settings():
    #import pdb;pdb.set_trace()
    return render_template("index.html")


@app.route("/inquiry")
def inquiry():
    return render_template("index.html")


# add user
"""
@app.route('/users', methods=['POST'])
def create_user():
    posted = request.get_json()
    if 'name' in posted:
        name = posted['name']
        user = User(name)
        db.session.add(user)
        db.session.commit()
        msg = 'User {} created'.format(user.user_id)
    else:
        msg = 'No user created'
    json = {
        'message': msg
    }
    return jsonify(json)
"""

# place
@app.route('/users/<string:userid>/places', methods=['GET'])
def get_place(userid):
    userid = str(userid)
    user = db.session.query(User).filter_by(user_id=userid).first()
    json = {
        'place': user.place
    }
    return jsonify(json)


@app.route('/users/<string:userid>/places', methods=['PUT'])
def update_place(userid):
    userid = str(userid)
    user = db.session.query(User).filter_by(user_id=userid).first()
    posted = request.get_json()
    if 'place' in posted:
        user.place = posted['place']
        db.session.add(user)
        db.session.commit()
        msg = 'User {} {} updated'.format(user.user_id, user.place)
    else:
        msg = 'No user updated'
    json = {
        'message': msg
    }
    return jsonify(json)

# prefer
@app.route('/users/<string:userid>/prefers', methods=['GET'])
def get_prefer(userid):
    userid = str(userid)
    print("userid", userid)
    user = db.session.query(User).filter_by(user_id=userid).first()
    print("user", user)
    json = {
        'prefer': user.prefer
    }
    return jsonify(json)


@app.route('/users/<string:userid>/prefers', methods=['PUT'])
def update_prefer(userid):
    userid = str(userid)
    user = db.session.query(User).filter_by(user_id=userid).first()
    posted = request.get_json()
    if 'prefer' in posted:
        user.prefer = posted['prefer']
        db.session.add(user)
        db.session.commit()
        msg = 'User {} {} updated'.format(user.user_id, user.prefer)
    else:
        msg = 'No user updated'
    json = {
        'message': msg
    }
    return jsonify(json)

"""
# visit time
@app.route('/users/<string:userid>/visit_times', methods=['GET'])
def get_visit_time(userid):
    userid = str(userid)
    user = db.session.query(User).filter_by(user_id=userid).first()
    user_visit_time = user.visit_time
    str_visit_time = user_visit_time.strftime('%H:%M')
    json = {
        'visit_time': str_visit_time
    }
    return jsonify(json)


@app.route('/users/<string:userid>/visit_times', methods=['PUT'])
def update_visit_time(userid):
    userid = str(userid)
    user = db.session.query(User).filter_by(user_id=userid).first()
    posted = request.get_json()
    if 'visit_time' in posted:
        str_visit_time = posted['visit_time']
        dt_visi_time = datetime.datetime.strptime(str_visit_time, '%H:%M')
        user.visit_time = dt_visi_time
        db.session.add(user)
        db.session.commit()
        msg = 'User {} {} updated'.format(user.user_id, str_visit_time)
    else:
        msg = 'No user updated'
    json = {
        'message': msg
    }
    return jsonify(json)
"""

# budget
@app.route('/users/<string:userid>/budgets', methods=['GET'])
def get_budget(userid):
    userid = str(userid)
    user = db.session.query(User).filter_by(user_id=userid).first()
    json = {
        'budget': str(user.budget)
    }
    return jsonify(json)


@app.route('/users/<string:userid>/budgets', methods=['PUT'])
def update_budget(userid):
    userid = str(userid)
    user = db.session.query(User).filter_by(user_id=userid).first()
    posted = request.get_json()
    if 'budget' in posted:
        user.budget = int(posted['budget'])
        db.session.add(user)
        db.session.commit()
        msg = 'User {} {} updated'.format(user.user_id, user.budget)
    else:
        msg = 'No user updated'
    json = {
        'message': msg
    }
    return jsonify(json)
