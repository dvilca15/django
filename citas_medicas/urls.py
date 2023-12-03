from django.urls import path
from .views import AgendarCita, ListaCitas, ListaCitasAdmin

app_name = 'citas_medicas'

citas_patterns = [
    path('agendar/', AgendarCita.as_view(), name='agendar_cita'),
    path('citas/', ListaCitas.as_view(), name='lista_citas'),
    path('citas_admin/', ListaCitasAdmin.as_view(), name='lista_citas_admin'),
    
]

urlpatterns = citas_patterns
