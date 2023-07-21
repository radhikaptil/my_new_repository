from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def string3(request):
    return HttpResponse('<i><h1> This is a string3 </h1></i>')
def string4(request):
    return HttpResponse('<marquee><h1> This is a string4 </h1></marquee>')