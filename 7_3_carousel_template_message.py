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
    carousel_template_message = TemplateSendMessage(
        alt_text='Carousel template',
        template=CarouselTemplate(
            columns=[
                CarouselColumn(
                    thumbnail_image_url='https://i.imgur.com/vgFbdDK.jpg',
                    title='參加網聚',
                    text='請問你想參加哪一場網聚',
                    actions=[
                        PostbackAction(
                            label='2021/5/1',
                            display_text='我想參加2021/5/1的時段',
                            data='action=meetup&itemid=1'
                        ),
                        PostbackAction(
                            label='2021/6/1',
                            display_text='我想參加2021/6/1的時段',
                            data='action=meetup&itemid=2'
                        ),
                        PostbackAction(
                            label='2021/7/1',
                            display_text='我想參加2021/7/1的時段',
                            data='action=meetup&itemid=3'
                        )
                        # MessageAction(
                        #     label='message1',
                        #     text='message text1'
                        # ),
                        # URIAction(
                        #     label='uri1',
                        #     uri='http://example.com/1'
                        # )
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url='https://i.imgur.com/SYP9lpm.jpg',
                    title='線上家教',
                    text='請預約線上家教的時段',
                    actions=[
                        PostbackAction(
                            label='2021/5/1',
                            display_text='我想參加2021/5/1的時段',
                            data='action=tutor&itemid=1'
                        ),
                        PostbackAction(
                            label='2021/6/1',
                            display_text='我想參加2021/6/1的時段',
                            data='action=tutor&itemid=2'
                        ),
                        PostbackAction(
                            label='2021/7/1',
                            display_text='我想參加2021/7/1的時段',
                            data='action=tutor&itemid=3'
                        )
                        # MessageAction(
                        #     label='message2',
                        #     text='message text2'
                        # ),
                        # URIAction(
                        #     label='uri2',
                        #     uri='http://example.com/2'
                        # )
                    ]
                )
            ]
        )
    )
    line_bot_api.reply_message(event.reply_token, carousel_template_message)
    
    
# run app
if __name__ == "__main__":
    app.run(host='127.0.0.1', port=5566,debug="True")