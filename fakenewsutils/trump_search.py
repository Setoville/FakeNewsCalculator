
def num_instances(article, search_word):
    num = 0
    g = article.split(" ")
    for word in g:
        if (word == search_word):
            num = num+1

    return num
