from __future__ import unicode_literals

from django.conf import settings
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _

from utils.gerador_hash import gerar_hash


class AtividadeFisica(models.Model):
    #1 campo da tupla fica no banco de dados
    #2 campo da tupla eh mostrado para o usuario
    TIPOS = (
        ('AERÓBICA', 'Aeróbica'),
        ('ANAERÓBICA', 'Anaeróbica'),
        ('ALONGAMENTO', 'Alongamento'),
    )

    nome = models.CharField(_('Nome da atividade *'), unique=True, max_length=25, help_text='* Campos obrigatórios')
    descricao = models.TextField(_('Detalhes da atividade física'), null=True, blank=True, max_length=1000, help_text='Se necessário, explique a atividade física')
    tipo = models.CharField(_('Tipo de atividade *'), max_length=15, choices=TIPOS, help_text='Em relação ao consumo de oxigênio')
    
    slug = models.SlugField('Hash',max_length= 200,null=True,blank=True)

    
    class Meta:
        ordering            =   ['nome']
        verbose_name        =   _('atividade_fisica')
        verbose_name_plural =   _('atividades_fisicas')

    def __str__(self):
         return '%s | %s' % (self.nome, self.tipo)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = gerar_hash()
        self.nome = self.nome.upper()
        super(AtividadeFisica, self).save(*args, **kwargs)

    @property
    def get_absolute_url(self):
        return reverse('atividade_fisica_update', args=[str(self.id)])

    @property
    def get_delete_url(self):
        return reverse('atividade_fisica_delete', args=[str(self.id)])
