from flask import Flask
from flask_cors import CORS
import http.client

app = Flask(__name__)

@app.route('/article',methods=['GET','POST'])
def parse_article():
    if request.method == 'POST':
        return request.form['articleURL']
    if request.method == 'GET':
        return "hello world"