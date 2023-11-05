from django.shortcuts import render, redirect
from .forms import formulario_contacto
from .models import Contacto

# Create your views here.

def contacto(request):
    if request.method == "POST":
        form_contacto = formulario_contacto(data=request.POST)
        if form_contacto.is_valid():
            nombre = request.POST.get("nombre")
            email = request.POST.get("email")
            contenido = request.POST.get("contenido")
            
        
            contacto = Contacto(nombre=nombre, email=email, contenido=contenido)
            contacto.save()

            return redirect("/contacto/?valido")
    else:
        form_contacto = formulario_contacto()

    return render(request, "contacto/contacto.html", {'mi_formulario': form_contacto})