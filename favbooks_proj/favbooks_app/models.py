from django.db import models
from login_app.models import User

class Manager(models.Manager):
    def validator(self, postData):
        errors = {}
        if postData['title'] == '':
            errors['title'] = "A title is required"
        if len(postData['description']) < 5:
            errors['description'] = "Description must be at least 5 characters"
        return errors

class Book(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(default="Default")
    users_who_like = models.ManyToManyField(User, related_name = 'liked_books')
    uploaded_by = models.ForeignKey(User, related_name = 'books_uploaded', on_delete = models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = Manager()