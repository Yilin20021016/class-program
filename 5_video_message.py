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
line_bot_api = LineBotApi('nD7u6mhkk5CwLs8w/iuM5wf4p5kbWoA7W/nWUHBSZNePvIw/n4/f73SMdMYeYiPVh6GFohOvim2V2k4LuWH0kykqQPzuUYkLsud0OXZZiF/lxjyNqWVuim1/OhxfUhLBlJIr2QDKoCCe8INmfAo4KQdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('e3c17505cd5456d3024eb949b26fffcb')

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

    # line_bot_api.reply_message(event.reply_token, StickerSendMessage(package_id='446',sticker_id='1988'))

    # line_bot_api.reply_message(event.reply_token, ImageSendMessage(original_content_url='https://i.imgur.com/Ae3QqtC.jpeg', 
    #                                                                 preview_image_url='https://i.imgur.com/Ae3QqtCb.jpg'))

    line_bot_api.reply_message(event.reply_token, VideoSendMessage(original_content_url='https://www.youtube.com/02878ce7-ad1c-41f8-a8a7-331ef8ba77ca',
                                                                    preview_image_url='https://th.bing.com/th?id=OVP.MF5nEI-4O6uJQja1d_fLiQHgFo&w=288&h=162&c=7&rs=1&qlt=90&o=5&pid=2.1'))

# run app
if __name__ == "__main__":
    app.run(host='127.0.0.1', port=5566,debug="True")