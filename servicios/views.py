from django.shortcuts import render, redirect
from servicios.models import Servicio, ServicioForm
from .forms import FormularioServicios

# Create your views here.
def servicios(request):
    servicios=Servicio.objects.all() 
    return render(request, "servicios/servicios.html", {"servicios":servicios})

# Para el formulario

def servicios(request):
    if request.method == "POST":
        form_servicios = FormularioServicios(data=request.POST)
        if form_servicios.is_valid():
            nombre = request.POST.get("nombre")
            email = request.POST.get("email")
            servicio = request.POST.get("servicio")
            
            nuevo_servicio = ServicioForm(nombre=nombre, email=email, servicio=servicio)
            nuevo_servicio.save()

            return redirect("/servicios/?valido")
    else:
        form_servicios = FormularioServicios()

    return render(request, "servicios/servicios.html", {'mi_formulario': form_servicios})
