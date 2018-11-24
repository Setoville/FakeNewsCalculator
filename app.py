from flask import Flask
from flask_cors import CORS
import http.client

app = Flask(__name__)

@app.route('/article',methods=['GET','POST'])
def parse_article():
    if request.method == 'POST':
        print (request.form.get("articleURL"))
        return "hello world"
    
@app.route('/hello',methods=['GET'])
def hello_world():
    print (request.headers['articleURL'])
    return "hello world"