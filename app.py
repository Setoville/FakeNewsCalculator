from flask import Flask
from flask import request
from flask import jsonify
from flask_cors import CORS
from random import randint
import http.client

app = Flask(__name__)

@app.route('/article',methods=['GET','POST'])
def parse_article():
    if request.method == 'POST':
        print (request.form.get("articleURL"))
        return "hello world"
    
@app.route('/test',methods=['GET'])
def hello_world():
    print (request.headers['articleURL'])
    return "hello world"

@app.route('/random',methods=['GET'])
def random():
    return jsonify(
        score=randint(0,100)
    )
