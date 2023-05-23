from django.shortcuts import render, HttpResponse
  
context = {
  'nombre': 'Pimienta',
  'edad': 489, 
  'gustos': ['dormir', 'comer', 'maullar']
}

def index(request):
  return render(request, "indexapp1.html", context)