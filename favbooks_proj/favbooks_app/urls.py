from django.urls import path
from . import views

urlpatterns = [
    path('home', views.home),
    path('add_book', views.addBook),
    path('<int:id>', views.bookview, name='bookview'),
    path('fav/<int:id>', views.fav),
    path('my_favs', views.my_favs),
    path('update/<int:id>', views.update),
    path('delete/<int:id>', views.delete),
    path('clear', views.clear)
]