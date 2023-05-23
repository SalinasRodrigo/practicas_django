from django.urls import path
from . import views

app_name = 'getpostapp'
urlpatterns = [
    path('', views.index),
    path('users', views.create_user, name='process')
]