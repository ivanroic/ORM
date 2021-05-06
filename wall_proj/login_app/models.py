from django.db import models
from datetime import datetime
import re

class Manager(models.Manager):
    def reg_validator(self, postData):
        errors = {}
        if len(postData['first_name']) < 2:
            errors["first_name"] = "First Name should be at least 5 characters"
        if len(postData['last_name']) < 2:
            errors["last_name"] = "Last Name should be at least 5 characters"
        
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(postData['email']):
            errors['email'] = "Invalid Email"
        if len(User.objects.filter(email=postData['email'])) > 0:
            errors['email'] = "Email already exists"

        if postData['password'] != postData['confirm_pw']:
            errors['password'] = "Passwords must match"
        if len(postData['password']) < 8:
            errors["password"] = "Password must contain at least 8 characters"

        if datetime.strptime(postData['birthday'],"%Y-%m-%d") > datetime.now():
            errors['birthday'] = "Birthday must be prior to current date"

        born = datetime.strptime(postData['birthday'],"%Y-%m-%d")
        def calculateAge(born):
            today = datetime.today()
            try:
                birthday = born.replace(year = today.year)
            except ValueError:
                birthday = born.replace(year = today.year, month = born.month + 1, day = 1)
            if birthday > today:
                return today.year - born.year - 1
            else:
                return today.year - born.year

        if calculateAge(born) <= 13:
            errors['birthday'] = "User must be at least 13 years of age"

        return errors

    def login_validator(self, postData):
        errors = {}
        if len(User.objects.filter(email=postData['email_login'])) == 0:
            errors['email_login'] = 'Email Not Found'
        return errors

class User(models.Model):
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    birthdate = models.DateField()
    email = models.CharField(max_length=30)
    password = models.CharField(max_length=25)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = Manager()