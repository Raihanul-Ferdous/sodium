from django.urls import path
from .import views



urlpatterns = [
    path('', views.home, name='profile1'),
    #path('', views.users, name='profile'),
]
