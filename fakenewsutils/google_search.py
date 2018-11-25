#from py_bing_search import PyBingWebSearch
import requests
import json
import re

def article_title_search(title):
    num_results = 0
    subscription_key = "8b7bd7038e824cb08e38fca1dc911442"
    assert subscription_key
    search_url = "https://api.cognitive.microsoft.com/bing/v7.0/search"
    search_term = "title"

    headers = {"Ocp-Apim-Subscription-Key" : subscription_key}
    params  = {"q": search_term, "textDecorations":True, "textFormat":"HTML"}
    response = requests.get(search_url, headers=headers, params=params)
    response.raise_for_status()
    search_results = response.json()
    print(search_results)

    # API KEYS: )1) 8b7bd7038e824cb08e38fca1dc911442 (2) 22a7de0a131844cca5b0afe8f242f751

    return num_results

print (article_title_search("different title"))
