# import flask related
from flask import Flask, request, abort
from urllib.parse import parse_qsl
# import linebot related
from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
    LocationSendMessage, ImageSendMessage, StickerSendMessage,
    VideoSendMessage, TemplateSendMessage, ButtonsTemplate, PostbackAction, MessageAction, URIAction,
    PostbackEvent, ConfirmTemplate, CarouselTemplate, CarouselColumn,
    ImageCarouselTemplate, ImageCarouselColumn, FlexSendMessage
)
import json

# create flask server
app = Flask(__name__)
line_bot_api = LineBotApi('Qvc5Y2XQlt5cSU1ZBLqStTavXDhvQvdzDP667LvboIYzWs/I162t2UoWD8gSzhW5+klN5UdBqBb5QPHGmq5/OjSSfWIyPQtEWeoVguNCbjrz778ws/GG9w+OZpC8VQuLSLib688e2suntCL/bOJkfAdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('1e34a3dd333ccb5329b5d48f0119e480')

@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        print('receive msg')
        handler.handle(body, signature)
    except InvalidSignatureError:
        print("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)
    return 'OK'

# handle msg
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    # get user info & message
    user_id = event.source.user_id
    msg = event.message.text
    user_name = line_bot_api.get_profile(user_id).display_name
    
    # get msg details
    print('msg from [', user_name, '](', user_id, ') : ', msg)

    # line_bot_api.reply_message(event.reply_token, TextSendMessage(text = msg))

    line_bot_api.reply_message(event.reply_token, StickerSendMessage(package_id='11539',sticker_id='52114120'))

# run app
if __name__ == "__main__":
    app.run(host='127.0.0.1', port=5566)