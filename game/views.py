from django.shortcuts import render,redirect
import random
from django.http import HttpResponse
# View to start the game and set a random number in session
def start_game(request):
    request.session['number'] = random.randint(1, 10)
    return redirect('home')

# View to handle guessing
def home(request):
    number = (request.session.get('number'))
    message = ''

    if request.method == 'POST':

        guess = int(request.POST.get('nbr'))
        
        if guess < number:
            message = f'{guess} is too low! '
        elif guess > number:
            message = f'{guess} is too high! '
        else:
            message ='correct'
    print(message)
    return render(request, 'main.html', {'message': message})

