from django.urls import path
from .views import AgendarCita


citas_patterns = [
    path('agendar/', AgendarCita.as_view(), name='agendar_cita'),
    # Agrega otras URLs según sea necesario
]
