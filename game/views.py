from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from . import guess_game
def home(request):
    nbr=guess_game.guess_fun(2)
    print(nbr)
    return render(request,'main.html',{'nbr':nbr})