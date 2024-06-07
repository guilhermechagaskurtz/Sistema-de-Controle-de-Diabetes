from __future__ import unicode_literals

from django.apps import apps
from django.conf import settings
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, UserManager
from django.db import models
from django.db.models import Q
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _

from datetime import timedelta, datetime

from utils.gerador_hash import gerar_hash

class AdministradorAtivoManager(UserManager):
    def get_queryset(self):
        return super().get_queryset().filter(tipo='ADMINISTRADOR', is_active=True)


class ClienteAtivoManager(UserManager):
    def get_queryset(self):
        return super().get_queryset().filter(tipo='CLIENTE', is_active=True)


class Usuario(AbstractBaseUser):
    #1 campo da tupla fica no banco de dados
    #2 campo da tupla eh mostrado para o usuario
    TIPOS_USUARIOS = (
        ('ADMINISTRADOR', 'Administrador'),
        ('CLIENTE', 'Cliente'),
        ('MÉDICO', 'Médico' ),
        ('NUTRICIONISTA', 'Nutricionista'),
        ('EDUCADOR FÍSICO', 'Educador Físico' ),
        ('DEGUSTANDO', 'Degustando' ),
    ) 
    TIPO_SEXO = (
        ('MASCULINO', 'Masculino'),
        ('FEMININO', 'Feminino'),
    )

    USERNAME_FIELD = 'email'

    tipo = models.CharField(_('Tipo do usuário *'), max_length=19, choices=TIPOS_USUARIOS, default='CLIENTE', help_text='* Campos obrigatórios')
    nome = models.CharField(_('Nome completo *'), max_length=100)
    email = models.EmailField(_('Email'), unique=True, max_length=100, db_index=True)
    cpf = models.CharField(_('CPF *'),max_length=14,help_text='ATENÇÃO: Somente os NÚMEROS')
    fone = models.CharField(_('Celular par contato *'),max_length=14, help_text='ATENÇÃO: Somente os NÚMEROS')

    data_nascimento = models.DateField(_("Data de nascimento *"), null=True, blank=True, auto_now=False, auto_now_add=False, help_text='dd/mm/aaaa')
    sexo = models.CharField(_('Sexo *'), max_length=10, choices=TIPO_SEXO, null=True, blank=True, help_text='Campo obrigatório para cálculo de gasto energético/calórico e consumo alimentar')    
    altura = models.DecimalField(_('Altura (metros) *'), max_digits=3, decimal_places=2, null=True, blank=True,) 
    
    
    # peso = models.DecimalField(_('Peso (Kg) *'), max_digits=5, decimal_places=2, null=True, blank=True,)
    # imc = models.DecimalField(_('Índice de Massa Corporal (calculado)'), max_digits=3, decimal_places=2,null=True, blank=True,) 
    # percentual_gordura = models.DecimalField(_('Percentual de gordura (%)'), max_digits=3, decimal_places=0,null=True, blank=True, help_text='Número inteiro (sem casas decimais)') 
    
    is_active = models.BooleanField(_('Ativo'), default=False, help_text='Se ativo, o usuário tem permissão para acessar o sistema')
    slug = models.SlugField('Hash',max_length= 200,null=True,blank=True)

    objects = UserManager()
    administradores = AdministradorAtivoManager()
    clientes = ClienteAtivoManager()

    class Meta:
        ordering            =   ['tipo','nome']
        verbose_name        =   _('usuário')
        verbose_name_plural =   _('usuários')

    def __str__(self):
        return '%s | %s' % (self.nome, self.email)

    def has_module_perms(self, app_label):
        return True

    def has_perm(self, perm, obj=None):
        return True

    def get_short_name(self):
        return self.nome[0:15].strip()

    def get_full_name(self):
        return self.nome

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = gerar_hash()
        self.nome = self.nome.upper()
        if not self.id:
            self.set_password(self.password) #criptografa a senha digitada no forms
        super(Usuario, self).save(*args, **kwargs)

    def get_id(self):
        return self.id

    @property
    def is_staff(self):
        if self.tipo == 'ADMINISTRADOR':
            return True
        return False

    @property
    def get_absolute_url(self):
        return reverse('usuario_update', args=[str(self.id)])

    @property
    def get_delete_url(self):
        return reverse('usuario_delete', args=[str(self.id)])

    @property
    def get_usuario_register_activate_url(self):
        return '%s%s' % (settings.DOMINIO_URL, reverse('usuario_register_activate', kwargs={'slug': self.slug}))
    
    @property
    def get_submissoes(self):
        return apps.get_model('submissao', 'Submissao').objects.filter(aluno=self)

    @property
    def get_submissao_create_url(self):
        return '%s?usuario_id=%d' % (reverse('submissao_create'), self.id)
