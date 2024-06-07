from __future__ import unicode_literals
from django.conf.urls import url

from core.views import HomeRedirectView

from .views import (DadosClienteUpdateView, HomeView, AboutView)

urlpatterns = [
   url(r'^home$', HomeView.as_view(), name='cliente_home'), 
   url(r'^$', HomeRedirectView.as_view(), name='home_redirect'),
   url(r'^about$', AboutView.as_view(), name='cliente_about'),
   url(r'^meus-dados/$', DadosClienteUpdateView.as_view(), name='cliente_dados_update'),
]
