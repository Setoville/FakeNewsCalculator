from flask import Flask
from flask import request
from flask import jsonify
from flask_cors import CORS
from random import randint
import base64
import http.client

app = Flask(__name__)


@app.route('/article',methods=['GET'])
def parse_article():
    
    encodedArticleURLfromHeader = request.args.get('articleURL',default = None,type=str)

    if articleURLfromHeader is not None:
        #decode base64
        decodedArticleURLfromHeader = base64.b64decode(encodedArticleURLfromHeader)

        print (decodedArticleURLfromHeader)
        return 0

    
    return 1

@app.route('/random',methods=['GET'])
def random():
    return jsonify(
        score=randint(0,100)
    )
