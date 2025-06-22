#flask  https://flask.palletsprojects.com/en/stable/
#Flask 和 Django 都是 Python 常用的 Web 框架  https://www.perplexity.ai/search/python-min-ru-he-shi-yong-qing-IKspVcELRvGQd6hECJaqjQ8
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<H1>Hello, World!帥哥~~~</H1>"

#flask --app app run  (第2個APP 使檔名) 修改時要關閉再啟動
#flask --app app run --debug  修改時不需關閉再啟動，自己會關閉重啟