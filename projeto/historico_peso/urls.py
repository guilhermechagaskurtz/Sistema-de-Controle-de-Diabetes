from django.conf.urls import url

from .views import HistoricoPesoListView, HistoricoPesoCreateView
from .views import HistoricoPesoUpdateView, HistoricoPesoDeleteView


urlpatterns = [
	url(r'list/$', HistoricoPesoListView.as_view(), name='historico_peso_list'),
	url(r'cad/$', HistoricoPesoCreateView.as_view(), name='historico_peso_create'),
	# url(r'(?P<pk>\d+)/$', HistoricoPesoUpdateView.as_view(), name='historico_peso_update'),
	url(r'(?P<pk>\d+)/delete/$', HistoricoPesoDeleteView.as_view(), name='historico_peso_delete'),
]
