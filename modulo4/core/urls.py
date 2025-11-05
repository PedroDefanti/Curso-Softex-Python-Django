from django.urls import path
from . import views

urlpatterns = [
    path(
        '',
        views.home,
        name='home',),
    path(
        'call/',
        views.call,
        name='call',),
]