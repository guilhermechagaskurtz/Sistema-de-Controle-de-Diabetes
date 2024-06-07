from django import forms
from registro_atividade.models import RegistroAtividade
from usuario.models import Usuario

class ClienteForm(forms.ModelForm):
    cliente = forms.ModelChoiceField(label='Cliente ou paciente', queryset=Usuario.clientes.all())
                                     

    class Meta:
        model = RegistroAtividade
        fields = ['cliente', 'data', 'hora', 'atividade', 'duracao', 'esforco', 'frequencia_cardiaca_media']
        
        



class BuscaAtividadeForm(forms.Form):
    cliente = forms.CharField(label='Cliente de pesquisa', required=False)
    atividade = forms.CharField(label='Atividade a ser pesquisada', required=False)
    data = forms.CharField(label='Data de pesquisa', required=False, help_text='Pesquise por dia ou mês ou ano ou data dd/mm/aaaa')