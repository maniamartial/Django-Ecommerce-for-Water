from django.http.response import HttpResponse
from django.shortcuts import render

# Create your views here.


def hello(request):
    return HttpResponse('<h1>Maria DB or MongoDB</h2>')
