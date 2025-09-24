from django.shortcuts import render, HttpResponse
import random

topics = [
    {'id': 1, 'title': 'routing', 'body': 'Routing is...'},
    {'id': 2, 'title': 'view', 'body': 'view is...'},
    {'id': 3, 'title': 'moodel', 'body': 'moddel is...'}
]


# Create your views here.
def HTMLTemplate():
    global topics
    ol = ''  ##변수 생성
    for topic in topics:
        ol += f'<li><a href="/read/{topic["id"]}">{topic["title"]}</a></li>'
    return f'''
    <html>
    <body>
    <h1>Django</h1>
    <ol>
        {ol}
    </ol>
    <h2>Welcome</h2>
    Hello Django!
    </body>
    </html>
    '''


def index(request):
    return HttpResponse(HTMLTemplate())


def create(request):
    return HttpResponse("Create!")


def read(request, id):
    return HttpResponse("Read!" + id)
