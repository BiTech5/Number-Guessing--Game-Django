from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from . import guess_game
def home(request):
    a=guess_game.guess_fun(2)
    print(a)
    return HttpResponse(f'<h1>Hello World</h1> {a}')