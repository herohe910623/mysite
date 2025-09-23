from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def create(request):
    return HttpResponse("Create!")

def read(request):
    return HttpResponse("Read!")