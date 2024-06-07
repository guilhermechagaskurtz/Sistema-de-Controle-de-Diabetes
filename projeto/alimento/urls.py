from django.conf.urls import url

from .views import AlimentoListView, AlimentoCreateView
from .views import AlimentoUpdateView, AlimentoDeleteView


urlpatterns = [
	url(r'list/$', AlimentoListView.as_view(), name='alimento_list'),
	url(r'cad/$', AlimentoCreateView.as_view(), name='alimento_create'),
	url(r'(?P<pk>\d+)/$', AlimentoUpdateView.as_view(), name='alimento_update'),
	url(r'(?P<pk>\d+)/delete/$', AlimentoDeleteView.as_view(), name='alimento_delete'),
]
