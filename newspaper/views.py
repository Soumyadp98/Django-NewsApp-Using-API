from django.shortcuts import render
from newsapi import NewsApiClient
# # Create your views here.


def index(request):
    newsApi = NewsApiClient(api_key= 'a99a74e3b7d6414e9cdfb5832732e741')
    headLines =newsApi.get_top_headlines(sources='bbc-news')
    articles=headLines['articles']
    desc=[]
    news=[]
    img=[]
    auth=[]
    for i in range(len(articles)):
        article=articles[i]
        desc.append(article['description'])
        news.append(article['title'])
        img.append(article['urlToImage'])
        auth.append(article['author'])
    mylist=zip(news,desc,img,auth)
    return render(request,"main/index.html", context={"mylist":mylist})