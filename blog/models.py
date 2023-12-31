from django.db import models
from django.contrib.auth.models import User
from .forms import BLOG_CHOICES

# Create your models here.

class Categoria(models.Model):
    nombre = models.CharField(max_length=50)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = 'categoria'
        verbose_name_plural = 'categorias'
         
    def __str__(self):
        return self.nombre
    
class Post(models.Model):
    titulo = models.CharField(max_length=50)
    contenido = models.CharField(max_length=50)
    imagen = models.ImageField(upload_to="blog", null=True, blank=True)
    autor  = models.ForeignKey(User, on_delete=models.CASCADE)
    categorias = models.ManyToManyField(Categoria)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = 'post'
        verbose_name_plural = 'posts'
         
    def __str__(self):
        return self.titulo



class PostBlog(models.Model):
    categoria = models.CharField(max_length=50, choices=BLOG_CHOICES)
    post = models.CharField(max_length=255)

    def __str__(self):
        return self.post