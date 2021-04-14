from django.urls import path
from . import views

urlpatterns = [
    path('main', views.main),
    path('add_dojo', views.add_dojo),
    path('add_ninja', views.add_ninja),
    path('delete', views.delete),
]