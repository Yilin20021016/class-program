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
    confirm_template_message = TemplateSendMessage(
        alt_text='Confirm template',
        template=ConfirmTemplate(
            text='是否確定匯款100元?',
            actions=[
                PostbackAction(
                    label='是',
                    display_text='我確定款款100元',
                    data='action=pay'
                ),
                PostbackAction(
                    label='否',
                    display_text='才不要',
                    data='action=nopay'
                )
                # MessageAction(
                #     label='是',
                #     text='我確定款款100元'
                # ),
                # MessageAction(
                #     label='否',
                #     text='才不要'
                # )
            ]
        )
    )
    line_bot_api.reply_message(event.reply_token, confirm_template_message)
    
    
# run app
if __name__ == "__main__":
    app.run(host='127.0.0.1', port=5566,debug="True")