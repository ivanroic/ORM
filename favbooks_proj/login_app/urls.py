from django.urls import path     
from . import views

urlpatterns = [
    path('root', views.main),
    path('register', views.register),
    path('success', views.success, name='success'),
    path('clear', views.delete),
    path('login', views.login, name='login'),
    path('logout', views.logout),
]