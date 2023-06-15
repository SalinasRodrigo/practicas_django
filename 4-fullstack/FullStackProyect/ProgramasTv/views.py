from django.shortcuts import render, redirect
from .models import Show, Network
# Create your views here.
def index(request):
  context = {"all_shows": Show.objects.all()} 
  return render (request, "index.html", context)

def show_one(request, id):
  print(Show.objects.get(id=id))
  context={"show": Show.objects.get(id=id)}
  
  return render (request, "show_one.html", context)

def new(request):
  context = {"all_networks": Network.objects.all()} 
  return render (request, "new.html", context)


def create(request):
  if request.method == "POST":
    print (request.POST)
    my_network=Network.objects.get(id=request.POST['network_id'])
    print (my_network)
    Show.objects.create(title = request.POST['title'], description = request.POST['description'], release_date = request.POST['release_date'],
                         network = my_network)
    return redirect("/")
  if request.method == "GET":
    return redirect("/new")
  
def update(request, id):
  context = {"all_networks": Network.objects.all(),
             "show": Show.objects.get(id=id)} 
  return render (request, "update.html", context)

def update_process(request, id):
  if request.method == "POST":
    print (request.POST)
    my_network=Network.objects.get(id=request.POST['network_id'])
    my_show = Show.objects.get(id=id)
    my_show.title = request.POST['title']
    my_show.release_date = request.POST['release_date']
    my_show.description = request.POST['description']
    my_show.network = my_network
    my_show.save()
    return redirect("/")
  if request.method == "GET":
    return redirect("/update/"+id)


def delete(request, id):
  if request.method == "POST":
    to_delete = Show.objects.get(id=id)
    to_delete.delete()
    return redirect("/")
  if request.method == "GET":
    return redirect("/")
