from django import forms
from .models import CitaMedica

class CitaMedicaForm(forms.ModelForm):
    class Meta:
        model = CitaMedica
        fields = ['nombre', 'fecha', 'hora', 'motivo']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre'}),
            'fecha': forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'Fecha'}),
            'hora': forms.TimeInput(attrs={'class': 'form-control', 'placeholder': 'Hora'}),
            'motivo': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Motivo'}),
        }
