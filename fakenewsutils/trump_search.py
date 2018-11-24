
def num_trumps(article, search_word):
    num = 0
    g = article.split(" ")
    for word in g:
        if (word == search_word):
            num = num+1

    return num


x = num_trumps("Trump Trump lel yeet Trump", "Trump")
print (x)
