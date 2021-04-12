from django.urls import path     
from . import views
urlpatterns = [
    path('root', views.main),
    path('process_money', views.money),
    path('reset', views.reset),
]