from django import forms

BLOG_CHOICES = [
    ('Social Media', 'Social Media'),
    ('Desarrollo Web', 'Desarrollo Web'),
    ('Diseño Gráfico', 'Diseño Gráfico'),
]

class FormularioBlog(forms.Form):
    categoria = forms.ChoiceField(label="Categoría", choices=BLOG_CHOICES)
    post = forms.CharField(label="Nombre del Post", required=True )

