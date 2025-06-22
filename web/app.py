#flask  https://flask.palletsprojects.com/en/stable/
#Flask 和 Django 都是 Python 常用的 Web 框架  https://www.perplexity.ai/search/python-min-ru-he-shi-yong-qing-IKspVcELRvGQd6hECJaqjQ8

#flask --app app run  (第2個APP 使檔名) 修改時要關閉再啟動
#flask --app app run --debug  修改時不需關閉再啟動，自己會關閉重啟

from flask import Flask, request, abort
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import *
from google import genai
from dotenv import load_dotenv
import os

app = Flask(__name__)
client = genai.Client(api_key=os.environ['Gemini_API_KEY'])


line_bot_api = LineBotApi(os.environ['CHANNEL_ACCESS_TOKEN'])
handler = WebhookHandler(os.environ['CHANNEL_SECRET'])

@app.route("/")
@app.route("/<string:question>")
def index(question:str=""):
    response = client.models.generate_content(
    model="gemini-2.5-flash", contents=f"{question},回應請輸出成為html格式")
    html_format = response.text
    html_format = html_format.replace("```html","").replace("```","")
    return html_format


@app.route("/callback", methods=['POST'])
def callback():
    signature = request.headers['X-Line-Signature']
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    return 'OK'

@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    #response = model.generate_content(event.message.text)
    response = client.models.generate_content(
    model="gemini-2.5-flash", contents=event.message.text
    )
    message = TextSendMessage(text=response.text)
    #line_bot_api.reply_message(event.reply_token, message)
    line_bot_api.reply_message(event.reply_token, '200')
