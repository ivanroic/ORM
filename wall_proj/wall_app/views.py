from django.shortcuts import render, redirect
from .models import Message, Comment
from login_app.models import User

def main(request):
    if 'user_id' not in request.session:
        return redirect('/login_reg/root')
    context = {
        'active_user': User.objects.get(id=request.session['user_id']),
        'all_messages': Message.objects.all(),
        'all_comments': Comment.objects.all(),
    }
    return render(request, 'wall.html', context)

def postMessage(request):
    active_user = User.objects.get(id=request.session['user_id'])
    Message.objects.create(message = request.POST['post_message'], user = active_user)
    new_message = Message.objects.last()
    id = new_message.id
    return redirect('/wall/main')

def postComment(request):
    active_user = User.objects.get(id=request.session['user_id'])
    message_comment = Message.objects.get(id=request.POST['message_comment_id'])
    Comment.objects.create(comment = request.POST['post_comment'], user = active_user, message = message_comment)
    new_comment = Comment.objects.last()
    id = new_comment.id
    return redirect('/wall/main')

def delete(request, id):
    Message.objects.get(id=id).delete()
    return redirect('/wall/main')