from django.db import models

class Dojos(models.Model):
    name = models.CharField(max_length=50)
    city = models.CharField(max_length=25)
    state = models.CharField(max_length=25)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Ninjas(models.Model):
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    dojo = models.ForeignKey(Dojos, related_name="ninja", on_delete = models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)