from django.shortcuts import HttpResponse, redirect, render
from django.http import JsonResponse

# Create your views here.
def index(request):
  return render(request, "indexBlogs.html")

def new(request):
  return HttpResponse("placeholder para mostrar un nuevo formulario para crear un nuevo blog")

def create(request):
  return redirect("/")

def show(request, id):
  return HttpResponse(f"placeholder para mostrar el blog numero: {id}")

def edit(request, id):
  return HttpResponse(f"placeholder para editar el blog {id}")

def destroy(request, id):
  return redirect("/")

def json(request):
  return JsonResponse({"foo": "bar"})
