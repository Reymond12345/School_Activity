from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def greet(request, name):
    return HttpResponse("Hello " + name.capitalize() + ", Welcome to USLS")

def index(request):
    return HttpResponse("This is my highschool page")

def about(request):
    return HttpResponse("This is my about page")