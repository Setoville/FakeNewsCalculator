import json

def data_compare():

        with open('tweets.json') as data_file:
                #data is dict
                data = json.load(data_file)
                tweetList = data['tweets']

        for tweet in tweetList:
                print (tweet['text'])
        

data_compare()