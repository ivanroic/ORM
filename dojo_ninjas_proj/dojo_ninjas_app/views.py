from django.shortcuts import render, redirect
from .models import Dojos, Ninjas

def main(request):
    context = {
        "all_dojos": Dojos.objects.all(),
        "all_ninjas": Ninjas.objects.all(),
    }
    return render(request, "dojo_ninjas_app/index.html", context)

def add_dojo(request):
    Dojos.objects.create(name = request.POST['name'], city = request.POST['city'], state = request.POST['state'])
    return redirect('/main')

def add_ninja(request):
    Ninjas.objects.create(first_name = request.POST['first'], last_name = request.POST['last'], dojo = Dojos.objects.get(id=request.POST['dojo_id']))
    return redirect('/main')

def delete(request):
    c = dojo.ninja.all
    c.delete()
    return redirect('/main')

    # c = Ninjas.objects.all()
    # c.delete()