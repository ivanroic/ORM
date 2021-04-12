from django.shortcuts import render
import random

random_num = random.randint(1, 100)
print(random_num)

def index(request):
    request.session['count'] = 0
    request.session['x'] = 'Neutral'
    return render(request, 'index.html')

def check(request):
    request.session['count'] = request.session['count']+1
    print(request.session['count'])

    if request.session['count'] > 5:
        request.session['x'] = 'Game Over, Try Again'
        request.session['count'] = 0
        print('Game Over')
    elif "guess" not in request.POST:
        request.session['x'] = 'Neutral'
    elif random_num == int(request.POST['guess']):
        request.session['x'] = 'Win'
        print('Correct!')
    elif  random_num > int(request.POST['guess']):
            request.session['x'] = 'Too Low'
            print('Too Low')
    else:
        request.session['x'] = 'Too High'
        print('Too High')
    return render(request, 'index.html')