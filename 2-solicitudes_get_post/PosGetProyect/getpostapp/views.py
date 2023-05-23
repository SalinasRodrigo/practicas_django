from django.shortcuts import render
def index(request):
    request.session.clear()
    return render(request,"index.html")

def create_user(request):
    request.session['name'] = request.POST['name']
    request.session['email'] = request.POST['email']
    

    return render(request,"show.html")