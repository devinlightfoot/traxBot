from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return(HttpResponse("You're at the traxBotWeb index"))

def about(request):
    return(HttpResponse("You're at the about page"))

def  trax(request):
    return(HttpResponse("You're at the trax page"))

def profile(request):
    return(HttpResponse("You're at the profile page"))

def products(request):
    return(HttpResponse("You're at the products page"))