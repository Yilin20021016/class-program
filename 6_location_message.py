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

    # line_bot_api.reply_message(event.reply_token, VideoSendMessage(original_content_url='https://video-atl3-2.xx.fbcdn.net/v/t39.25447-2/227238604_617110389727658_2441376736641369579_n.mp4?_nc_cat=111&vs=44004b1c42525818&_nc_vs=HBksFQAYJEdNeGlpdzJxSVpFMVFqRUNBT3RGYWY0MGdfRWhibWRqQUFBRhUAAsgBABUAGCRHQi1RM2dwc20xQkppcWtGQUhwT1FkcE9OYlZTYnY0R0FBQUYVAgLIAQBLBogScHJvZ3Jlc3NpdmVfcmVjaXBlATERZGlzYWJsZV9wb3N0X3B2cXMADXN1YnNhbXBsZV9mcHMAEHZtYWZfZW5hYmxlX25zdWIAIG1lYXN1cmVfb3JpZ2luYWxfcmVzb2x1dGlvbl9zc2ltAChjb21wdXRlX3NzaW1fb25seV9hdF9vcmlnaW5hbF9yZXNvbHV0aW9uABUAJQAcAAAmpLTR9InlfhUCKAJDMxgLdnRzX3ByZXZpZXccF0AthR64UeuFGCdkYXNoX2dlbjNiYXNpY181c2VjZ29wX2hxMV9mcmFnXzJfdmlkZW8SABgYdmlkZW9zLnZ0cy5jYWxsYmFjay5wcm9kOBJWSURFT19WSUVXX1JFUVVFU1QbCIgVb2VtX3RhcmdldF9lbmNvZGVfdGFnBm9lcF9oZBNvZW1fcmVxdWVzdF90aW1lX21zDTE2MzQyMzc1NDM2NzMMb2VtX2NmZ19ydWxlB3VubXV0ZWQTb2VtX3JvaV9yZWFjaF9jb3VudAkxMDQ2MTM4NjIMb2VtX3ZpZGVvX2lkDzI3ODgxNzgzMDU4MTI5NRJvZW1fdmlkZW9fYXNzZXRfaWQPMjc4ODEzNDMwNTgxNzM1FW9lbV92aWRlb19yZXNvdXJjZV9pZA8yNzg4MTM0MjcyNDg0MDIcb2VtX3NvdXJjZV92aWRlb19lbmNvZGluZ19pZA8zOTc4NjI4ODE2ODE2MzMlAhwAJb4BGweIAXMEOTQ4MgJjZAoyMDIxLTA1LTAyA3JjYgkxMDQ2MTM4MDADYXBwCVRlYW1TaWdodAJjdBlDT05UQUlORURfUE9TVF9BVFRBQ0hNRU5UE29yaWdpbmFsX2R1cmF0aW9uX3MGMTQuODQ4AnRzD29lcF9wcm9ncmVzc2l2ZQA%3D&ccb=1-5&_nc_sid=edb743&efg=eyJ2ZW5jb2RlX3RhZyI6Im9lcF9oZCJ9&_nc_ohc=Qr6fuUekVlAAX-i2TRc&_nc_ht=video-atl3-2.xx&edm=AGo2L-IEAAAA&oh=dcf746405471a57cfea7a3bdb9a455df&oe=616DC4B2&_nc_rid=bd7c13089182496&_nc_vts_prog=1&vts=1&_nc_vts_internal=1',
    #                                                                 preview_image_url='https://scontent.ftpe8-2.fna.fbcdn.net/v/t15.5256-10/fr/cp0/e15/q65/121943140_278817863914625_5271658409045053463_n.jpg?_nc_cat=103&ccb=1-5&_nc_sid=ccf8b3&efg=eyJpIjoidCJ9&_nc_ohc=GP_PxoL0uDkAX-Ulwy2&_nc_ht=scontent.ftpe8-2.fna&oh=cfa21f8dd004bef4fbc35f431a11b3c0&oe=616CC854'))

    line_bot_api.reply_message(event.reply_token, LocationSendMessage(title='Store Location',
                                                                        address='Taipei 101',
                                                                        latitude=25.033981,
                                                                        longitude=121.564506))

# run app
if __name__ == "__main__":
    app.run(host='127.0.0.1', port=5566,debug="True")