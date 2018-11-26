# from py_bing_search import PyBingWebSearch
import requests
import json
import re

def handle_bing_response(response, title):
    score = 0
    result_descriptions = json.dumps(response)
    split_words = result_descriptions.split(" ")
    split_title = title.split(" ")
    for description in split_words:
        for word in split_title:
            if word in description:
                score = score+1

    # at this point score will be high (indicating not that fake)
    # we should convert back 1 - 10 range of fake-ness
    if (score > 400):
        return 0
    elif (score > 360):
        return 1
    elif (score > 320):
        return 2
    elif (score > 280):
        return 3
    elif (score > 240):
        return 4
    elif (score > 200):
        return 5
    elif (score > 160):
        return 6
    elif (score > 120):
        return 7
    elif (score > 80):
        return 8
    elif (score > 40):
        return 9
    else:
        return 10

    return score

# lets search for the given article's title on Bing and find articles of similar title
def article_title_search(title):

    # enter api key here
    subscription_key = ""

    assert subscription_key
    search_url = "https://api.cognitive.microsoft.com/bing/v7.0/search"
    search_term = title

    headers = {"Ocp-Apim-Subscription-Key" : subscription_key}
    params  = {"q": search_term, "textDecorations":True, "textFormat":"HTML"}
    response = requests.get(search_url, headers=headers, params=params)
    response.raise_for_status()
    search_results = response.json()

    score = handle_bing_response(search_results, title)
    print(score)
    return score

