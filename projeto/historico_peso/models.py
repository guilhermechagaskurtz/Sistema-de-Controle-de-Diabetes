from __future__ import unicode_literals

from django.apps import apps
from django.conf import settings
from django.contrib.auth.models import  UserManager
from django.db import models
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _


from utils.gerador_hash import gerar_hash


class HistoricoPeso(models.Model):
    cliente = models.ForeignKey('usuario.Usuario', verbose_name='Cliente *', on_delete=models.PROTECT, help_text="* indica campo obrigatório.")
    data = models.DateField(_('Data de atualização de peso *'), help_text='Use dd/mm/aaaa')
    peso = models.DecimalField(_('Peso atual (Kg) *'), max_digits=5, decimal_places=2, null=True, blank=True,)
    imc = models.DecimalField(_('Índice de Massa Corporal (calculado)'), max_digits=5, decimal_places=2,null=True, blank=True) 
    tmb = models.DecimalField(_('Taxa Metabolismo Basal (calculado)'), max_digits=5, decimal_places=2,null=True, blank=True) 
    percentual_gordura = models.DecimalField(_('Percentual de gordura (%)'), max_digits=3, decimal_places=0,null=True, blank=True, help_text='Número inteiro (sem casas decimais)') 
    
    is_active = models.BooleanField(_('Ativo'), default=False, help_text='Se ativo, o usuário tem permissão para acessar o sistema')
    slug = models.SlugField('Hash',max_length= 200,null=True,blank=True)

    
    class Meta:
        ordering            =   ['cliente','-data']

    def __str__(self):
        return '%s | %s | %s' % (self.cliente.nome, self.data, self.peso)

    def save(self, *args, **kwargs):
        # capturar o usuario logado e coloca-lo como o cliente que esta fazendo sua atualização de peso
        
        if not self.slug:
            self.slug = gerar_hash()
            
        super(HistoricoPeso, self).save(*args, **kwargs)

    def get_id(self):
        return self.id

    @property
    def get_absolute_url(self):
        return reverse('historico_peso_update', args=[str(self.id)])

    @property
    def get_delete_url(self):
        return reverse('historico_peso_delete', args=[str(self.id)])

    