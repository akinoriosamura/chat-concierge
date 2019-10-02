import os

from chat import dialogue_manager
import chat.models
from chat.database import init_db, db
from chat.models.user import User

from flask import Flask, abort, request

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)


#  initialize app db migrate
def create_app():
    app = Flask(__name__)
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
manager = dialogue_manager.DialogueManager()


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

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    """
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=event.message.text))
    """
    print(event)
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text="sample"))


@app.route("/")
def test():
    app.logger.info("test OK")
    user = User("test")
    db.session.add(user)
    db.session.commit()

    return 'OK'
