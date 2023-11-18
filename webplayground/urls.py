
from django.contrib import admin
from django.urls import path, include
from pages.urls import pages_patterns
from django.conf import settings
from django.conf.urls.static import static
from profiles.urls import profiles_patterns
from citas_medicas.urls import citas_patterns


urlpatterns = [
        path('',include('core.urls')),
        path('pages/',include(pages_patterns)),
        path('admin/', admin.site.urls),
        
        #paquetes de autenticacion
        
        path('accounts/', include('django.contrib.auth.urls')),
        path('accounts/', include('registration.urls')),  # Asegúrate de que 'registration.urls' esté definido como una lista
        path('profiles/', include(profiles_patterns)),
        path('agendar/', include(citas_patterns)),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.PROFILE_MEDIA_ROOT)

