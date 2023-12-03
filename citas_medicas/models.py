# citas/models.py
from django.db import models
from pages.models import Page 

class CitaMedica(models.Model):
    
    ESTADO_CHOICES = [
        ('PROGRAMADA', 'Programada'),
        ('ATENDIDA', 'Atendida'),
    ]
    nombre = models.CharField(max_length=100, null=True, blank=True)
    fecha = models.DateField(null=True, blank=True)
    hora = models.TextField(null=True, blank=True)
    motivo = models.TextField(null=True, blank=True)
    page = models.ForeignKey(Page, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(null=True, blank=True,max_length=200)
    estado = models.CharField(null=True, blank=True,max_length=20, choices=ESTADO_CHOICES, default='PROGRAMADA')
    
    def __str__(self):
        return f'Cita de {self.nombre} el {self.fecha} a las {self.hora}'

