from django.shortcuts import render, redirect
from .models import Show
from django.contrib import messages

def all_shows(request):
    context = {
        'all_shows': Show.objects.all()
    }
    return render(request,'tv_shows_app/shows.html', context)

def add_page(request):
    return render(request, 'tv_shows_app/add_page.html')

def create(request):
    errors = Show.objects.basic_validator(request.POST)
    if len(errors) > 0:
        for v in errors.items():
            messages.error(request, v)
        return redirect('/add_page')

    Show.objects.create(title = request.POST['title'], network = request.POST['network'], release_date = request.POST['release_date'], description = request.POST['description'])
    created_show = Show.objects.last()
    id = created_show.id
    return redirect('show_view', id=id)

def show_view(request, id):
    context = {
        'chosen_show': Show.objects.get(id=id)
    }
    return render(request, 'tv_shows_app/show_view.html', context)

def back(request):
    return redirect('/shows')

def delete(request, id):
    show_to_delete = Show.objects.get(id=id)
    show_to_delete.delete()
    return redirect('/shows')

def edit(request, id):
    context = {
        'chosen_show': Show.objects.get(id=id)
    }
    return render(request, 'tv_shows_app/edit_page.html', context)

def update(request):
    errors = Show.objects.basic_validator(request.POST)
    if len(errors) > 0:
        for v in errors.items():
            messages.error(request, v)
        return redirect('edit_view')
    
    chosen_show = Show.objects.get(id=request.POST['showid'])
    chosen_show.title = request.POST['title']
    chosen_show.network = request.POST['network']
    chosen_show.release_date = request.POST['release_date']
    chosen_show.description = request.POST['description']
    chosen_show.save()
    id = chosen_show.id
    return redirect('show_view', id=id)