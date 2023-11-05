from django.db import models
from .forms import SERVICIOS_CHOICES

class Servicio(models.Model): 
    titulo = models.CharField(max_length=50)
    contenido = models.CharField(max_length=50)
    imagen = models.ImageField(upload_to="servicios")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = 'servicio'
        verbose_name_plural = 'servicios'
         
    def __str__(self):
        return self.titulo
    
# Para el formulario 

class ServicioForm(models.Model):
    nombre = models.CharField(max_length=255)
    email = models.EmailField()
    servicio = models.CharField(max_length=50, choices=SERVICIOS_CHOICES)

    def __str__(self):
        return self.nombre