from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def first(request):
    return HttpResponse('<h1>this is my first creation</h1>')

def second(request):
    return HttpResponse('<marquee><h1>This is my second creation</h1></marquee>')