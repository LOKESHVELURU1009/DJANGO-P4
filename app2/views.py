from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def new_first(request):
    return HttpResponse('<h1>this is app2 first creation</h1>')

def new_second(request):
    return HttpResponse('<marquee><h1>this is app2 second creation</h1></marquee>')