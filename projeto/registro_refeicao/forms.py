from django import forms
from alimento.models import Alimento
from registro_refeicao.models import RegistroRefeicao
from usuario.models import Usuario


class ClienteForm(forms.ModelForm):
    cliente = forms.ModelChoiceField(label='Cliente ou paciente', queryset=Usuario.clientes.all())
    

    class Meta:
        model = RegistroRefeicao
        fields = ['cliente', 'data', 'hora', 'alimento', 'quantidade']
        


class BuscaRefeicaoForm(forms.Form):
    cliente = forms.CharField(label='Cliente de pesquisa', required=False)
    alimento = forms.CharField(label='Alimento de pesquisa', required=False)
    data = forms.CharField(label='Data de pesquisa', required=False, help_text='Pesquise por dia ou mês ou ano ou data dd/mm/aaaa')