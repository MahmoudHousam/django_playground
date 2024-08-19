from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    return HttpResponse("Welcome to my book store")


def index2(request):
    return HttpResponse("Second welcome to my book store")
