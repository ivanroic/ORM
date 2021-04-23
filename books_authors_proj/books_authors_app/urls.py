from django.urls import path     
from . import views

urlpatterns = [
    path('book_main', views.book_main),
    path('add_book', views.add_book),
    path('<int:id>', views.book_view, name = 'book_view'),
    path('b', views.add_to_book),

    path('author_main', views.author_main),
    path('add_author', views.add_author),
    path('<int:id>/a', views.author_view),
    path('<int:id>/aa', views.add_to_author)

    # path('delete', views.delete)
]