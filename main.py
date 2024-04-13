# -*- coding: utf-8 -*-
"""
Created on Sat Mar 16 16:30:33 2024

@author: Mike

LINE Bot 股票下單
"""
import os
import yaml
from datetime import datetime
from loguru import logger
from pathlib import Path
from flask import Flask, request, abort, send_file
from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import *

from action import (
    sotck_command_parsing, 
    query_order, 
    refresh_stock_web, 
    take_screenshot, 
    sort_by_status,
    delete_order,
    query_my_shares,
    query_stock_No,
    shut_down,
)

time = datetime.now().strftime('%Y%m%d')
logger.add(f"./logs/log_{time}.log", rotation="00:00", format="{time} {level} {message}")


with open(Path(__file__).parent.joinpath('setting.yaml'), 'r') as file:
        setting = yaml.safe_load(file)
CHANNEL_ACCESS_TOKEN = setting.get('CHANNEL_ACCESS_TOKEN')
CHANNEL_SECRET = setting.get('CHANNEL_SECRET')
BASE_URL = setting.get('BASE_URL')
# Channel Access Token
line_bot_api = LineBotApi(CHANNEL_ACCESS_TOKEN)
# Channel Secret
handler = WebhookHandler(CHANNEL_SECRET)


app = Flask(__name__)
@app.route('/')
def index():
    return 'Hello World'

# 監聽所有來自 /callback 的 Post Request
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

@app.route('/screenshot')
def send_screenshot():
    photo_path = 'C:\\Users\\User\\Documents\\stock\\LINE_Bot\\screenshot.jpg'
    return send_file(photo_path, mimetype='image/jpeg')


command_list = [
            '重整頁面',
            '截圖',
            '查詢代碼',
            '查詢庫存',
            '查詢委託',            
            '排序狀態',
            '刪單',
            '下單',
            '關機',
            ]
# 處理訊息
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    msg_command = event.message.text
    logger.info(msg_command)        
    # handle command DEV
    try:
        command_splt = msg_command.split('\n')
        if command_splt[0]==command_list[0] and len(command_splt)==1:
            refresh_stock_web()
            reply_screenshot(event)
        elif command_splt[0]==command_list[1] and len(command_splt)==1:
            take_screenshot()
            reply_screenshot(event)
        elif command_splt[0]==command_list[2] and len(command_splt)==2:
            query_stock_No(command_splt[1])
            reply_screenshot(event)
        elif command_splt[0]==command_list[3] and len(command_splt)==1:
            query_my_shares()
            reply_screenshot(event)
        elif command_splt[0]==command_list[4] and len(command_splt)==1:
            query_order()
            reply_screenshot(event)
        elif command_splt[0]==command_list[5] and len(command_splt)==1:
            sort_by_status()
            reply_screenshot(event)
        elif command_splt[0]==command_list[6] and len(command_splt)==2:
            delete_order(int(command_splt[1]))
            reply_screenshot(event)
        elif command_splt[0]==command_list[7] and len(command_splt)==8:
            status = sotck_command_parsing(command_splt)
            if status:
                query_order()
            reply_screenshot(event)
        elif command_splt[0]==command_list[8] and len(command_splt)==1:
            shut_down()
        elif command_splt[0]=='Help' and len(command_splt)==1:
            msg = ''
            for c in  command_list:
                msg = msg+c+'\n'
            line_bot_api.reply_message(event.reply_token, TextSendMessage(text=msg))
        else:
            line_bot_api.reply_message(event.reply_token, TextSendMessage(text='指令錯誤'))
    except Exception as e:
        message = TextSendMessage(text=str(e))
        line_bot_api.reply_message(event.reply_token, message)


def reply_screenshot(event):
    image_message = ImageSendMessage(
            original_content_url=BASE_URL+"/screenshot",
            preview_image_url=BASE_URL+"/screenshot"
            )

    line_bot_api.reply_message(event.reply_token, image_message)

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
