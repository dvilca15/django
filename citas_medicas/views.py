from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from .models import CitaMedica
from .forms import CitaMedicaForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

@method_decorator(login_required, name='dispatch')
class AgendarCita(CreateView):
    model = CitaMedica
    form_class = CitaMedicaForm
    template_name = 'citas_medicas/agendar_cita.html'
    success_url = reverse_lazy('agendar_cita')

