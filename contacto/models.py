from django.db import models
from datetime import datetime 

class Contacto(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField()
    contenido = models.TextField()
    created = models.DateTimeField(default=datetime.now, editable=False)
    updated = models.DateTimeField(auto_now=True)
   
    class Meta:
        verbose_name = 'contacto'
        verbose_name_plural = 'contactos'
         
    def __str__(self):
        return self.nombre