from django.urls import path     
from . import views
urlpatterns = [
    path('root', views.count),
    path('destroy_session', views.destroy),
    path('add_two', views.addTwo),
    path('increment', views.increment),
]