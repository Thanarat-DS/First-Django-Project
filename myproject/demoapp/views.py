from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse 
def hello(request): 
    return HttpResponse("Hello, world. This is the index view Demoapp.")

def pathview(request, name, id): 
    return HttpResponse("Name:{} UserID:{}".format(name, id)) 

def qryview(request): 
    name = request.GET['name'] 
    id = request.GET['id'] 
    return HttpResponse("Name:{} UserID:{}".format(name, id))

def showform(request): 
    return render(request, "form.html") 

def getform(request): 
    if request.method == "POST": 
        id=request.POST['id'] 
        name=request.POST['name'] 
    return HttpResponse("Name:{} UserID:{}".format(name, id)) 