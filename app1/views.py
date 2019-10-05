from django.shortcuts import render
from django.http import HttpResponse
from newsapi.newsapi_client import NewsApiClient

newsapi = NewsApiClient(api_key='fb839331b86f4965bf548b49797db34e')

k = newsapi.get_top_headlines(country="in",category="business")

temp = []
li = []
with open("C:/Users/user/Desktop/xnews/app1/data.txt") as f:
    for line in f:
        li.append(line)
def app_home(request):
    return render(request,'app1/app1.html')

def app_detail(request,slug):

    li.append(slug)
    f.close()
    hs = open("C:/Users/user/Desktop/xnews/app1/data.txt", "a")
    if (slug != "trending/"):
        hs.write(slug[:len(slug)-1:]+"\n")
    hs.close()

    if (slug == "business/"):
        k = newsapi.get_top_headlines(country="in", category="business")
        return render(request, "app1/news.html", k)

    elif (slug == "entertainment/"):
        k = newsapi.get_top_headlines(country="in", category="entertainment")
        return render(request, "app1/news.html", k)

    elif (slug == "general/"):
        k = newsapi.get_top_headlines(country="in", category="general")
        return render(request, "app1/news.html", k)

    elif (slug == "health/"):
        k = newsapi.get_top_headlines(country="in", category="health")
        return render(request, "app1/news.html", k)

    elif (slug == "science/"):
        k = newsapi.get_top_headlines(country="in", category="science")
        return render(request, "app1/news.html", k)

    elif (slug == "sports/"):
        k = newsapi.get_top_headlines(country="in", category="sports")
        return render(request, "app1/news.html", k)

    elif (slug == "technology/"):
        k = newsapi.get_top_headlines(country="in", category="technology")
        return render(request, "app1/news.html", k)
    elif (slug == "trending/"):
        word_counter = {}

        for word in li:
            if word in word_counter:
                word_counter[word] += 1
            else:
                word_counter[word] = 1


        popular_words = sorted(word_counter, key=word_counter.get, reverse=True)[:5]
        popular_words  = filter(None, popular_words)
        popular_words = filter(lambda a: a != 'trending/', popular_words)

        send = []
        items = {}
        for i in popular_words:
            url = "http://127.0.0.1:8000/app1/"+i
            items = {'word':i,'url':url}
            send = send + [items]
            items ={}

        return render(request, "app1/te.html", {'trending':send,})

    else:
        k= newsapi.get_everything(q=slug[:len(slug)-1:])

        return render(request, "app1/news.html", k)

