from django.http import HttpResponse

#from django.shortcuts import render

# Create your views here.

def posts(request):
    return HttpResponse("Hello, posts")