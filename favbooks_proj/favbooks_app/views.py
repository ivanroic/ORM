from django.http import request
from django.shortcuts import render, redirect
from login_app.models import User
from django.contrib import messages
from .models import Book

def home(request):
    if 'user_id' not in request.session:
        redirect ('/login_reg_root')
    context = {
        'active_user': User.objects.get(id=request.session['user_id']),
        'all_books': Book.objects.all(),
        'all_users': User.objects.all(),
    }
    return render(request, 'home.html', context)

def addBook(request):
    errors = Book.objects.validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/fb/home')
    else:
        active_user = User.objects.get(id=request.session['user_id'])
        print(active_user.birthdate)
        new_book = Book.objects.create(title = request.POST['title'], description = request.POST['description'], uploaded_by = active_user)
        active_user.liked_books.add(new_book)
        return redirect('/fb/home')

def bookview(request, id):
    context = {
        'active_user': User.objects.get(id=request.session['user_id']),
        'all_users': User.objects.all(),
        'all_books': Book.objects.all(),
        'chosen_book': Book.objects.get(id=id)
    }
    print(id)
    return render(request, 'bookview.html', context)

def update(request, id):
    errors = Book.objects.validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('bookview', id=id)
    else:
        book = Book.objects.get(id=id)
        book.title = request.POST['title']
        book.description = request.POST['description']
        book.save()
        messages.success(request, "Book Details Successfully Updated")
        return redirect('/fb/home')

def fav(request, id):
    active_user = User.objects.get(id=request.session['user_id'])
    chosen_book = Book.objects.get(id=id)
    if active_user not in chosen_book.users_who_like.all():
        active_user.liked_books.add(chosen_book)
        return redirect('/fb/home')
    else:
        active_user.liked_books.remove(chosen_book)
        return redirect('/fb/home')

def my_favs(request):
    context = {
        'active_user': User.objects.get(id=request.session['user_id']),
        'all_books': Book.objects.all(),
    }
    return render(request, 'favs.html', context)

def delete(request, id):
    chosen_book = Book.objects.get(id=id)
    chosen_book.delete()
    return redirect('/fb/home')

def clear(request):
    c = Book.objects.all()
    c.delete()
    return redirect('/fb/home')