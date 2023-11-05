from django.shortcuts import render, HttpResponse

def home(request): 
    return render(request, "proyecto_web/index.html")


