from django.shortcuts import render
from django.http import HttpResponse
from .models import Position
# Create your views here.
def index(request):
    return(render(request, 'traxBotWeb/index.html'))

def about(request):
    return(HttpResponse("You're at the about page"))

def  trax(request):
    pos = Position.objects.all()
    arr = []
    for p in pos:
        temp = '(%f, %f)' % (p.xPos, p.yPos)
        arr.append(temp)
    ret = '\n'.join(arr)
    print(ret)
    return(HttpResponse(ret))

def profile(request):
    return(HttpResponse("You're at the profile page"))

def products(request):
    return(HttpResponse("You're at the products page"))