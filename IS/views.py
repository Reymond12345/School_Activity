from django.shortcuts import render

def index(request):
    return render(request, 'IS/index.html')

def about(request):
    return render(request, 'IS/about.html')

# Create your views here.
