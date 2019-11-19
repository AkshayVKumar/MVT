from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return HttpResponse("<h1>Welcome to Index Page</h1>")

def homepage(request):
    return render(request,'page1.html')

def page2(request):
    return render(request,'app/page2.html')

def sample(request):
    return render(request,'sample.html')