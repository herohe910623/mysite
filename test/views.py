from django.shortcuts import render, HttpResponse
import random

topics = [
    {'id': 1, 'title': 'routing', 'body': 'Routing is...'},
    {'id': 2, 'title': 'view', 'body': 'view is...'},
    {'id': 3, 'title': 'moodel', 'body': 'moddel is...'}
]


# Create your views here.
def HTMLTemplate(articleTag):
    global topics
    ol = ''  ##변수 생성
    for topic in topics:
        ol += f'<li><a href="/read/{topic["id"]}">{topic["title"]}</a></li>'
    return f'''
    <html>
    <body>
    <h1><a href='/'>Django</a></h1>
    <ol>
        {ol}
    </ol>
        {articleTag}
    </body>
    </html>
    '''


def index(request):
    article = '''
    <h2>Welcome</h2>
    Hello Django!
    '''
    return HttpResponse(HTMLTemplate(article))


def create(request):
    article = '''
    <h2>Create</h2>
    '''
    return HttpResponse(article)


def read(request, id):
    global topics
    for topic in topics:
        if topic["id"] == int(id):
            article = f'<h2>{topic["title"]}</h2>{topic["body"]}'
    return HttpResponse(HTMLTemplate(article))
