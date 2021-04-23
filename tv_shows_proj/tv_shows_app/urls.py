from django.urls import path     
from . import views

urlpatterns = [
    path('shows', views.all_shows),
    path('add_page', views.add_page),
    path('create', views.create),
    path('show/<int:id>', views.show_view, name='show_view'),
    path('delete/<int:id>', views.delete),
    path('show/<id>/edit', views.edit, name='edit_view'),
    path('show/update', views.update, name='update'),
    path('edit', views.update),
]