from django import forms
from django.core.exceptions import ValidationError
from .models import CitaMedica, Page
from django.utils import timezone

class CitaMedicaForm(forms.ModelForm):
    class Meta:
        model = CitaMedica
        fields = ['nombre', 'fecha', 'hora', 'motivo', 'page','estado']
        widgets = {
            'fecha': forms.DateInput(attrs={'class': 'form-control', 'type': 'date', 'placeholder': 'Fecha'}),
            'hora': forms.Select(attrs={'class': 'form-control'}),
            'page': forms.Select(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.update_available_hours()

    def update_available_hours(self):
        # Obtén las horas ya agendadas para la fecha y la página actual
        fecha = self.cleaned_data.get('fecha') if hasattr(self, 'cleaned_data') and self.cleaned_data else None
        page = self.cleaned_data.get('page') if hasattr(self, 'cleaned_data') and self.cleaned_data else None
        booked_hours = CitaMedica.objects.filter(fecha=fecha, page=page).values_list('hora', flat=True)

        # Todas las horas fijas
        horas_fijas = [
            ('09:00 - 10:00 AM', '09:00 - 10:00 AM'),
            ('10:00 - 11:00 AM', '10:00 - 11:00 AM'),
            ('11:00 - 12:00 PM', '11:00 - 12:00 PM'),
            ('12:00 - 13:00 PM', '12:00 - 13:00 PM'),  
            ('13:00 - 14:00 PM', '13:00 - 14:00 PM'),  
            ('14:00 - 15:00 PM', '14:00 - 15:00 PM'),
            ('15:00 - 16:00 PM', '15:00 - 16:00 PM'),
        ]

        # Filtra las horas disponibles excluyendo las ya agendadas
        available_hours = [(value, label) for value, label in horas_fijas if value not in booked_hours]

        # Asigna las opciones al campo de hora
        self.fields['hora'].choices = available_hours

    def clean(self):
        cleaned_data = super().clean()
        fecha = cleaned_data.get('fecha')
        hora = cleaned_data.get('hora')
        page = cleaned_data.get('page')
        
        if fecha and fecha < timezone.now().date():
            raise ValidationError('No puedes agendar citas en fechas pasadas. Por favor, elige una fecha futura.')

        if fecha and hora:
            overlapping_appointments = CitaMedica.objects.filter(
                fecha=fecha,
                hora=hora,
                page=page
            )
            if self.instance.pk:
                overlapping_appointments = overlapping_appointments.exclude(pk=self.instance.pk)
            if overlapping_appointments.exists():
                raise ValidationError('Ya hay una cita agendada en este horario. Por favor, elige otra hora.')

        return cleaned_data
