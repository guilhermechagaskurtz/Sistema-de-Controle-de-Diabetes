from django.conf.urls import url

from .views import AtividadeFisicaListView, AtividadeFisicaCreateView
from .views import AtividadeFisicaUpdateView, AtividadeFisicaDeleteView


urlpatterns = [
	url(r'list/$', AtividadeFisicaListView.as_view(), name='atividade_fisica_list'),
	url(r'cad/$', AtividadeFisicaCreateView.as_view(), name='atividade_fisica_create'),
	url(r'(?P<pk>\d+)/$', AtividadeFisicaUpdateView.as_view(), name='atividade_fisica_update'),
	url(r'(?P<pk>\d+)/delete/$', AtividadeFisicaDeleteView.as_view(), name='atividade_fisica_delete'),
]
