from django.urls import path
from blogs import views

urlpatterns = [
    path('', views.index),
    path('new/', views.new),
    path('create/', views.create),
    path('<int:id>/', views.show),
    path('<int:id>/edit/', views.edit),
    path('<int:id>/delete/', views.destroy),
    path('json/', views.json)
]