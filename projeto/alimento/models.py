from __future__ import unicode_literals

from django.conf import settings
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _

from utils.gerador_hash import gerar_hash


class Alimento(models.Model):
    descricao = models.CharField(_('Descrição do alimento *'), max_length=100, help_text='Seja sucinto na descrição do alimento. Lembre que é campo obrigatório')
    unidade = models.CharField(_('Unidade do alimento *'), max_length=100, help_text='copo de 400 ml, ou colher, ou fatia, ou porção, por exemplo')
    calorias = models.DecimalField(_('Quantidade de calorias (g) da unidade desse alimento *'), max_digits=5, decimal_places=0, help_text='Quantidade de calorias para a unidade definida desse alimento') 
    carboidratos = models.DecimalField(_('Quantidade de carboidratos (g) da unidade desse alimento *'), max_digits=5, decimal_places=0, help_text='Quantidade de carboidratos para a unidade definida desse alimento') 
    fonte = models.CharField(_('Fonte ou referência desse alimento'), null = True, blank = True, max_length=100, help_text='Use como referência alguma instituição, ou artigo, ou livro, por exemplo')
    slug = models.SlugField('Hash',max_length= 200,null=True,blank=True)

    
    class Meta:
        ordering            =   ['descricao']
        verbose_name        =   _('alimento')
        verbose_name_plural =   _('alimentos')

    def __str__(self):
         return '%s | %s' % (self.descricao, self.unidade)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = gerar_hash()
        self.descricao = self.descricao.upper()
        super(Alimento, self).save(*args, **kwargs)

    @property
    def get_absolute_url(self):
        return reverse('alimento_update', args=[str(self.id)])

    @property
    def get_delete_url(self):
        return reverse('alimento_delete', args=[str(self.id)])
