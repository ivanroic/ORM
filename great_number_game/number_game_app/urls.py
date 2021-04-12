from django.urls import path
from . import views
urlpatterns = [
    path('root', views.index),
    path('check', views.check)
]