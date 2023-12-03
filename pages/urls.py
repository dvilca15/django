from django.urls import path
from . import views
from .views import PagesListView,PagesDetailView,PageCreate,PageUpdate,PageDelete
from .views import PagesListView, PagesDetailView, PageCreate, PageUpdate, PageDelete
from citas_medicas.views import AgendarCita



pages_patterns = ([
    path('', PagesListView.as_view(), name='pages'),
    path('<int:pk>/<slug:slug>/', PagesDetailView.as_view(), name='page'),
    path('create/', PageCreate.as_view(), name='create'),
    path('update/<int:pk>/', PageUpdate.as_view(), name='update'),
    path('delete/<int:pk>/', PageDelete.as_view(), name='delete'),
    path('agendar/', AgendarCita.as_view(), name='agendar_cita'),
],'pages')  
