# en tuapp/models.py
from django.db import models

class CitaMedica(models.Model):
    nombre = models.CharField(max_length=100, null=True, blank=True)
    fecha = models.DateField(null=True, blank=True)
    hora = models.TimeField(null=True, blank=True)
    motivo = models.TextField(null=True, blank=True)
    sasasasas = models.TextField(null=True, blank=True)

    def __str__(self):
        return f'Cita de {self.nombre} el {self.fecha} a las {self.hora}'

