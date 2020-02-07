import os
import datetime

from chat import dialogue_manager
import chat.models
from chat.models.user import User
from chat.database import init_db, db

from flask import Flask, abort, request, jsonify, render_template

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage, LocationMessage
)


#  initialize app db migrate
def create_app(test=False):
    app = Flask(
        __name__, static_folder="../build/static", template_folder="../build"
    )
    if test:
        app.config.from_object('chat.config.TestingConfig')
    else:
        app.config.from_object('chat.config.Config')
    init_db(app)

    return app


app = create_app()

# LINE Access Token
YOUR_CHANNEL_ACCESS_TOKEN = os.environ["YOUR_CHANNEL_ACCESS_TOKEN"]
# LINE Channel Secret
YOUR_CHANNEL_SECRET = os.environ["YOUR_CHANNEL_SECRET"]

line_bot_api = LineBotApi(YOUR_CHANNEL_ACCESS_TOKEN)
handler = WebhookHandler(YOUR_CHANNEL_SECRET)

# initialize
manager = dialogue_manager.DialogueManager(30, 150)


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


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    """
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=event.message.text))
    """
    print(event)
    if event.type == "message":
        if (event.message.text == "おすすめ"):
            line_bot_api.reply_message(
                event.reply_token,
                [
                    TextSendMessage(text='近くのおすすめの店舗を紹介するから位置情報を送ってねん！'+ chr(0x10008D)),
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
    lat = event.message.latitude
    lon = event.message.longitude
    print("位置情報", event.message)

    # レコメンド内容取得

    # lineにメッセージ送信
    line_bot_api.reply_message(
        event.reply_token,
        [
            TextSendMessage(text='おすすめ店舗は＊＊です。'),
            TextSendMessage(text='またいつでも聞いてください！'),
        ]
    )

@app.route("/")
def settings():
    return render_template("index.html")


@app.route("/inquiry")
def inquiry():
    return render_template("index.html")


# add user
@app.route('/users', methods=['POST'])
def ceate_user():
    posted = request.get_json()
    if 'name' in posted:
        name = posted['name']
        user = User(name)
        db.session.add(user)
        db.session.commit()
        msg = 'User {} created'.format(user.name)
    else:
        msg = 'No user created'
    json = {
        'message': msg
    }
    return jsonify(json)

# place
@app.route('/users/<int:userid>/places', methods=['GET'])
def get_place(userid):
    userid = str(userid)
    user = db.session.query(User).filter_by(id=userid).first()
    json = {
        'place': user.place
    }
    return jsonify(json)


@app.route('/users/<int:userid>/places', methods=['PUT'])
def update_place(userid):
    userid = str(userid)
    user = db.session.query(User).filter_by(id=userid).first()
    posted = request.get_json()
    if 'place' in posted:
        user.place = posted['place']
        db.session.add(user)
        db.session.commit()
        msg = 'User {} {} updated'.format(user.name, user.place)
    else:
        msg = 'No user updated'
    json = {
        'message': msg
    }
    return jsonify(json)

# prefer
@app.route('/users/<int:userid>/prefers', methods=['GET'])
def get_prefer(userid):
    userid = str(userid)
    user = db.session.query(User).filter_by(id=userid).first()
    json = {
        'prefer': user.prefer
    }
    return jsonify(json)


@app.route('/users/<int:userid>/prefers', methods=['PUT'])
def update_prefer(userid):
    userid = str(userid)
    user = db.session.query(User).filter_by(id=userid).first()
    posted = request.get_json()
    if 'prefer' in posted:
        user.place = posted['prefer']
        db.session.add(user)
        db.session.commit()
        msg = 'User {} {} updated'.format(user.name, user.prefer)
    else:
        msg = 'No user updated'
    json = {
        'message': msg
    }
    return jsonify(json)

# visit time
@app.route('/users/<int:userid>/visit_times', methods=['GET'])
def get_visit_time(userid):
    userid = str(userid)
    user = db.session.query(User).filter_by(id=userid).first()
    user_visit_time = user.visit_time
    str_visit_time = user_visit_time.strftime('%H:%M')
    json = {
        'visit_time': str_visit_time
    }
    return jsonify(json)


@app.route('/users/<int:userid>/visit_times', methods=['PUT'])
def update_visit_time(userid):
    userid = str(userid)
    user = db.session.query(User).filter_by(id=userid).first()
    posted = request.get_json()
    if 'visit_time' in posted:
        str_visit_time = posted['visit_time']
        dt_visi_time = datetime.datetime.strptime(str_visit_time, '%H:%M')
        user.visit_time = dt_visi_time
        db.session.add(user)
        db.session.commit()
        msg = 'User {} {} updated'.format(user.name, str_visit_time)
    else:
        msg = 'No user updated'
    json = {
        'message': msg
    }
    return jsonify(json)

# budget
@app.route('/users/<int:userid>/budgets', methods=['GET'])
def get_budget(userid):
    userid = str(userid)
    user = db.session.query(User).filter_by(id=userid).first()
    json = {
        'budget': str(user.budget)
    }
    return jsonify(json)


@app.route('/users/<int:userid>/budgets', methods=['PUT'])
def update_budget(userid):
    userid = str(userid)
    user = db.session.query(User).filter_by(id=userid).first()
    posted = request.get_json()
    if 'budget' in posted:
        user.budget = int(posted['budget'])
        db.session.add(user)
        db.session.commit()
        msg = 'User {} {} updated'.format(user.name, user.budget)
    else:
        msg = 'No user updated'
    json = {
        'message': msg
    }
    return jsonify(json)

# mail
@app.route('/users/<int:userid>/mails', methods=['GET'])
def get_mail(userid):
    userid = str(userid)
    user = db.session.query(User).filter_by(id=userid).first()
    json = {
        'mail': user.mail
    }
    return jsonify(json)


@app.route('/users/<int:userid>/mails', methods=['PUT'])
def update_mail(userid):
    userid = str(userid)
    user = db.session.query(User).filter_by(id=userid).first()
    posted = request.get_json()
    if 'mail' in posted:
        user.mail = posted['mail']
        db.session.add(user)
        db.session.commit()
        msg = 'User {} {} updated'.format(user.name, user.mail)
    else:
        msg = 'No user updated'
    json = {
        'message': msg
    }
    return jsonify(json)

# inquiry
@app.route('/users/<int:userid>/inquirys', methods=['GET'])
def get_inquiry(userid):
    userid = str(userid)
    user = db.session.query(User).filter_by(id=userid).first()
    json = {
        'inquiry': user.inquiry
    }
    return jsonify(json)


@app.route('/users/<int:userid>/inquirys', methods=['PUT'])
def update_inquiry(userid):
    userid = str(userid)
    user = db.session.query(User).filter_by(id=userid).first()
    posted = request.get_json()
    if 'inquiry' in posted:
        user.inquiry = posted['inquiry']
        db.session.add(user)
        db.session.commit()
        msg = 'User {} {} updated'.format(user.name, user.inquiry)
    else:
        msg = 'No user updated'
    json = {
        'message': msg
    }
    return jsonify(json)
