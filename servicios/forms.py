from django import forms


SERVICIOS_CHOICES = [
    ('Social Media', 'Social Media'),
    ('Desarrollo Web', 'Desarrollo Web'),
    ('Diseño Gráfico', 'Diseño Gráfico'),
]

class FormularioServicios(forms.Form):
    nombre = forms.CharField(label="Nombre", required=True)
    email = forms.CharField(label="Email", required=True)
    servicio = forms.ChoiceField(label="Servicio", choices=SERVICIOS_CHOICES)
