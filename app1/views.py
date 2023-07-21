from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def string1(request):
    return HttpResponse('<i><h1> This is a string1 </h1></i>')
def string2(request):
    return HttpResponse('<marquee><h1> This is a string2 </h1></marquee>')
