from django.shortcuts import render, redirect
import random

def main(request):
    if 'gold' not in request.session:
        request.session['gold'] = 0
    if 'act' not in request.session:
        request.session['act'] = []
    return render(request, "index.html")

def money(request):
    if 'farm' in request.POST:
        farm_num = random.randint(10, 20)
        request.session['gold'] = request.session['gold'] + int(farm_num)
        request.session['act'].append((f"Earned {int(farm_num)} gold from the Farm!"))

    elif 'cave' in request.POST:
        cave_num = random.randint(5, 10)
        request.session['gold'] = request.session['gold'] + int(cave_num)
        request.session['act'].append((f"Earned {int(cave_num)} gold from the Cave!"))

    elif 'house' in request.POST:
        house_num = random.randint(2, 5)
        request.session['gold'] = request.session['gold'] + int(house_num)
        request.session['act'].append((f"Earned {int(house_num)} gold from the House!"))
    
    elif 'casino' in request.POST:
        casino_num = random.randint(-50, 50)
        request.session['gold'] = request.session['gold'] + int(casino_num)
        request.session['act'].append((f"Earned/Lost {int(casino_num)} gold from the Casino!"))
    return redirect("/root")

def reset(request):
    request.session.clear()
    return redirect("/root")
    
