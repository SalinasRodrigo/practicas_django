from django.urls import path
from . import views

urlpatterns = [
    path("", views.index),
    path("new", views.new),
    path("create", views.create),
    path("show/<int:id>", views.show_one),
    path("update/<int:id>", views.update),
    path("update/<int:id>/process", views.update_process),
    path("delete/<int:id>", views.delete),
]