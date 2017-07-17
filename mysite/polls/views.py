from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse('Hello Worls from Polls')

# Create your views here.
