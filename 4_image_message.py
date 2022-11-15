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
    if "帽子" in msg:
        line_bot_api.reply_message(event.reply_token, ImageSendMessage(original_content_url='https://th.bing.com/th/id/R.071b3bdf704b7a5c49489959d6b86a20?rik=GqBR7PxZyOGIGg&riu=http%3a%2f%2fww3.sinaimg.cn%2fbmiddle%2f9150e4e5ly1fh2670pb7gj206a05xq34.jpg&ehk=GnQ%2bIhzkFR7vtby%2bUwJvSDB1H%2fGdFFS8kl3TnvjZnGk%3d&risl=&pid=ImgRaw&r=0', 
                                                                       preview_image_url='https://th.bing.com/th/id/R.071b3bdf704b7a5c49489959d6b86a20?rik=GqBR7PxZyOGIGg&riu=http%3a%2f%2fww3.sinaimg.cn%2fbmiddle%2f9150e4e5ly1fh2670pb7gj206a05xq34.jpg&ehk=GnQ%2bIhzkFR7vtby%2bUwJvSDB1H%2fGdFFS8kl3TnvjZnGk%3d&risl=&pid=ImgRaw&r=0'))
    else:
        line_bot_api.reply_message(event.reply_token, ImageSendMessage(original_content_url='https://th.bing.com/th/id/R.fee338d6708592e916805c434621405c?rik=HO7uMc0ndm5oJg&pid=ImgRaw&r=0',
                                                                        preview_image_url='https://th.bing.com/th/id/R.fee338d6708592e916805c434621405c?rik=HO7uMc0ndm5oJg&pid=ImgRaw&r=0'))
# run app
if __name__ == "__main__":
    app.run(host='127.0.0.1', port=5566,debug="True")