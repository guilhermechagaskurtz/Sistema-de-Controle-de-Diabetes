from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'', include('core.urls')),
    url(r'alimento/', include('alimento.urls')),
    url(r'atividade_fisica/', include('atividade_fisica.urls')),
    url(r'cliente/', include('cliente.urls')),
    url(r'historico_peso/', include('historico_peso.urls')),
    url(r'registro_atividade/', include('registro_atividade.urls')),
    url(r'registro_refeicao/', include('registro_refeicao.urls')),
    url(r'usuario/', include('usuario.urls')),
    url(r'^accounts/', include('django.contrib.auth.urls')),
]

#url para arquivos de media quando em desenvolvimento
if settings.DEBUG:
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += static(settings.STATIC_URL, 
    document_root = settings.STATIC_ROOT)    
  
