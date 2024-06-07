from django.conf.urls import url

from .views import RegistroRefeicaoListView, RegistroRefeicaoCreateView
from .views import RegistroRefeicaoUpdateView, RegistroRefeicaoDeleteView


urlpatterns = [
	url(r'list/$', RegistroRefeicaoListView.as_view(), name='registro_refeicao_list'),
	url(r'cad/$', RegistroRefeicaoCreateView.as_view(), name='registro_refeicao_create'),
	url(r'(?P<pk>\d+)/$', RegistroRefeicaoUpdateView.as_view(), name='registro_refeicao_update'),
	url(r'(?P<pk>\d+)/delete/$', RegistroRefeicaoDeleteView.as_view(), name='registro_refeicao_delete'),
]
