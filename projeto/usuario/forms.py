from django import forms
from .models import Usuario

class UsuarioRegisterForm(forms.ModelForm):
    TIPOS_USUARIOS = (
        ('CLIENTE', 'Cliente'),
    )

    tipo = forms.ChoiceField(label='Tipo *',choices=TIPOS_USUARIOS, help_text='Este processo cadastra somente alunos' )
    nome = forms.CharField(label='Nome completo', help_text='* Campos obrigatórios')
    email = forms.EmailField(label= 'Email *', max_length=100, help_text='Use o email institucional')
    
    cpf = forms.CharField(label='CPF *' , max_length = 14 , help_text='ATENÇÃO: Somente os NÚMEROS', required = True)
    
    fone = forms.CharField(label='Celular para contato *', max_length=14, help_text="ATENÇÃO: Somente os NÚMEROS", required = True)    
    password = forms.CharField(label= "Senha *", widget=forms.PasswordInput)
        
    class Meta:
        model = Usuario
        fields = ['nome','tipo', 'email', 'cpf', 'fone','password']


class BuscaUsuarioForm(forms.Form):
    TIPOS_USUARIOS = (
        (None, "---------"),
        ('ADMINISTRADOR', 'Administrador'),
        ('CLIENTE', 'Cliente'),
        ('MÉDICO', 'Médico' ),
        ('NUTRICIONISTA', 'Nutricionista'),
        ('EDUCADOR FÍSICO', 'Educador Físico' ),
        ('DEGUSTANDO', 'Degustando' ),
    ) 
    nome_usuario = forms.CharField(label='Nome do usuário', required=False)
    tipo = forms.ChoiceField(label='Tipo de usuário', choices=TIPOS_USUARIOS, required=False)