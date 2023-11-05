from django.shortcuts import render,  redirect
from blog.models import Post, PostBlog
from .forms import FormularioBlog


# Create your views here.
def blog(request): 
    posts=Post.objects.all()
    return render(request, "blog/blog.html", {"posts": posts})

# Para el formulario

def blog(request):
    if request.method == "POST":
        form_blog = FormularioBlog(data=request.POST)
        if form_blog.is_valid():
            categoria = request.POST.get("categoria")
            post = request.POST.get("post")
            
            nuevo_post = PostBlog(categoria=categoria, post=post)
            nuevo_post.save()

            return redirect("/blog/?valido")
    else:
        form_blog = FormularioBlog()

    return render(request, "blog/blog.html", {'mi_formulario': form_blog})