from django import forms
from django.core.validators import MaxValueValidator, MinValueValidator

from avaliacao.models import Avaliacao
from submissao.models import Submissao
from usuario.models import Usuario


class SubmissaoForm(forms.ModelForm):
    
    class Meta:
        model = Submissao
        fields = ['arquivo_documento_aceite', 'normativas', 'arquivo_texto_preprojeto', 'arquivo_texto_tfgorientador',
        'termo_autoria', 'arquivo_texto_tfgbanca', 'arquivo_texto_tfgrebanca', 'arquivo_texto_tfgfinal', 'termo_biblioteca',
        'arquivo_produto_tfgfinal', 'titulo', 'resumo', 'palavras_chave']
        
