from django import forms
from .models import aprendiz


class aprendizform(forms.ModelForm):
    class Meta:
        model = aprendiz
        fields = [
            'nombre',
            'apellido',
            'documento',
            'correo',
            'telefono',
            'tipo_de_documento',
            'ficha',
            'competencias',
            'fecha_nacimiento'
        ]

        widgets = {
            'fecha_nacimiento': forms.DateInput(
                attrs={'type': 'date'},
                format='%Y-%m-%d'
            )
        }