from django.conf.urls import url

from .views import RegistroAtividadeListView, RegistroAtividadeCreateView
from .views import RegistroAtividadeUpdateView, RegistroAtividadeDeleteView


urlpatterns = [
	url(r'list/$', RegistroAtividadeListView.as_view(), name='registro_atividade_list'),
	url(r'cad/$', RegistroAtividadeCreateView.as_view(), name='registro_atividade_create'),
	url(r'(?P<pk>\d+)/$', RegistroAtividadeUpdateView.as_view(), name='registro_atividade_update'),
	url(r'(?P<pk>\d+)/delete/$', RegistroAtividadeDeleteView.as_view(), name='registro_atividade_delete'),
]
