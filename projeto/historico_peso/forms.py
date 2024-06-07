from django import forms

from historico_peso.models import HistoricoPeso
from usuario.models import Usuario


class HistoricoPesoForm(forms.ModelForm):
    # cliente = forms.ModelChoiceField(label='Cliente ou paciente', queryset=Usuario.clientes.all())
    
    class Meta:
        model = HistoricoPeso
        fields = ['data', 'peso', 'percentual_gordura']
        


class BuscaHistoricoPesoForm(forms.Form):
    cliente = forms.CharField(label='Cliente de pesquisa', required=False)
    data = forms.CharField(label='Data de pesquisa', required=False, help_text='Pesquise por dia ou mês ou ano ou data dd/mm/aaaa')