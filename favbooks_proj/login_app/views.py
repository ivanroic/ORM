from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User
import bcrypt

def main(request):
    context = {
        'all_users': User.objects.all(),
    }
    return render(request, "main.html", context)

def register(request):
    errors = User.objects.reg_validator(request.POST)
        # check if the errors dictionary has anything in it
    if len(errors) > 0:
        # if the errors dictionary contains anything, loop through each key-value pair and make a flash message
        for key, value in errors.items():
            messages.error(request, value)
        # redirect the user back to the form to fix the errors
        return redirect('/login_reg/root')
    else:
        hashed_password = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt()).decode()
        # if the errors object is empty, that means there were no errors! A user will be created now..
        User.objects.create(first_name = request.POST['first_name'], last_name = request.POST['last_name'], email = request.POST['email'], birthdate = request.POST['birthday'], password = hashed_password)
        # Since a new user has been created, we can pass its ID to the success page so we can identify who has registered!
        new_user = User.objects.last()
        request.session['user_id'] = new_user.id
        return redirect('/login_reg/success')

def login(request):
    errors = User.objects.login_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/login_reg/root')
    else:
        potential_user = User.objects.filter(email=request.POST['email_login'])[0]
        if bcrypt.checkpw(request.POST['pw_login'].encode(),potential_user.password.encode()):
            request.session['user_id'] = potential_user.id
            print(request.session['user_id'])
            return redirect('/fb/home')
        else:
            messages.error(request, "Invalid Login", extra_tags='pw_login')
            return redirect('/login_reg/root')

def success(request):
    if 'user_id' not in request.session:
        return redirect('/login_reg/root')
    context = {
        'user': User.objects.get(id=request.session['user_id']),
    }
    return render(request, 'success.html', context)

def logout(request):
    request.session.clear()
    return redirect('/login_reg/root')

def delete(request):
    c = User.objects.all()
    c.delete()
    return redirect('/login_reg/root')