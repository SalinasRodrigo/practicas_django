from django.shortcuts import render
# otros imports
from .models import Movie
# muestra todos los datos de la tabla
def index(request):
    
    context = {
    	"all_the_movies": Movie.objects.all()
    }
    return render(request, "index.html", context)


