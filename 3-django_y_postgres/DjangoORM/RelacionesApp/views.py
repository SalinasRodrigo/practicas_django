from django.shortcuts import render
from .models import Author, Book

def index(request):
    context = {"authors": Author.objects.all()}		# sólo se envía todos los autores
    print(context)
    return render(request, "indexRelaciones.html", context)
