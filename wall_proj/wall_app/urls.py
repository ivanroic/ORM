from django.urls import path 
from . import views

urlpatterns = [
    path('main', views.main),
    path('post_message', views.postMessage),
    path('post_comment', views.postComment),
    path('delete/<int:id>', views.delete)
]