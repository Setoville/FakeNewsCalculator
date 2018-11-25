import json

def data_compare():

        with open('tweets.json') as data_file:
                #data is dict
                data = json.load(data_file)
                tweetList = data['tweets']

        parsed_tweets = []
        for tweet in tweetList:
                newJsonObject = {
                        "score": 100,
                        "tweet": tweet['text']
                }
                parsed_tweets.append(newJsonObject)
        
        for tweet in parsed_tweets:
                print (tweet)


data_compare()