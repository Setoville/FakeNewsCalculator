from flask import Flask
from flask import request
from flask_cors import CORS
from random import randint
import base64
import json
import urllib.request
import html2text

app = Flask(__name__)
CORS(app)

@app.route('/articleID/<articleURL>',methods=['GET'])
def parse_article(articleURL):
  #  encodedArticleURLfromHeader = request.args.get('articleURL',default = None,type=str)
    print (articleURL)

    if articleURL is not None:
        #decode base64
        decodedArticleURLfromHeader = base64.b64decode(articleURL).decode('utf-8')

        fp = urllib.request.urlopen(decodedArticleURLfromHeader)
        mybytes = fp.read()

        mystring = mybytes.decode("utf-8")
        fp.close()
        h = html2text.HTML2Text()
        print (h.handle(mystring))

        returnDict = {}

        returnDict.update({'decodedURL':decodedArticleURLfromHeader})

        jsonDataAsString = json.dumps(returnDict)

        return jsonDataAsString

    

@app.route('/random',methods=['GET'])
def random():
    return jsonify(
        score=randint(0,100)
    )
