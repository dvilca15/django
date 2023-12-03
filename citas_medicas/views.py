from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView,UpdateView
from django.utils.decorators import method_decorator
from django.contrib import messages
from django.views.generic import ListView
from .models import CitaMedica
from .forms import CitaMedicaForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator    
from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import get_object_or_404

@method_decorator(login_required, name='dispatch')
class AgendarCita(CreateView):
    model = CitaMedica
    form_class = CitaMedicaForm
    template_name = 'citas_medicas/agendar_cita.html'
    success_url = reverse_lazy('agendar_cita')

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.nombre = f"{self.request.user.first_name} {self.request.user.last_name}"
        selected_page = form.cleaned_data['page']
        form.instance.title = selected_page.title if selected_page else ''
        response = super().form_valid(form)

        messages.success(self.request, 'Cita agendada correctamente.')

        return response

    def form_invalid(self, form):

        print(form.cleaned_data)
        print(form.errors)

        messages.error(self.request, 'Error al agendar la cita. Verifica los datos ingresados.')

        return super().form_invalid(form)


@method_decorator(login_required, name='dispatch')
class ListaCitas(ListView):
    model = CitaMedica
    template_name = 'citas_medicas/lista_citas.html'
    context_object_name = 'citas'

    def get_queryset(self):
        return CitaMedica.objects.filter(nombre=self.request.user.get_full_name()).order_by('fecha', 'hora')


@method_decorator(staff_member_required, name='dispatch')
class ListaCitasAdmin(ListView):
    model = CitaMedica
    template_name = 'citas_medicas/lista_citas_admin.html'
    context_object_name = 'citas_admin'

    def get_queryset(self):
        return CitaMedica.objects.all().order_by('fecha', 'hora')
    
    
    

    