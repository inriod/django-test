from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def hello(request):
    response = HttpResponse("<h1>Hello World!</h1>")
    return response

def goodbye(request):
    response = HttpResponse("<h1>Goodbye!</h1>")
    return response

def index(request):
    response = HttpResponse("<h1>Welcome to the home page!</h1>")
    return response