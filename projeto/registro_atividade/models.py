from __future__ import unicode_literals

from django.conf import settings
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _

from utils.gerador_hash import gerar_hash


class RegistroAtividade(models.Model):
    #1 campo da tupla fica no banco de dados
    #2 campo da tupla eh mostrado para o usuario
    BORG = (
        ('7 - MUITO FÁCIL', '7 - Muito fácil'),
        ('9 - FÁCIL', '9 - Fácil'),
        ('11 - RELATIVAMENTE FÁCIL', '11 - Relativamente fácil'),
        ('13 - LIGEIRAMENTE CANSATIVO', '13 - Ligeiramente cansativo'),
        ('15 - CANSATIVO', '15 - Cansativo'),
        ('17 - MUITO CANSATIVO', '17 - Muito cansativo'),
        ('19 - EXAUSTIVO', '19 - Exaustivo'),
    )
    cliente = models.ForeignKey('usuario.Usuario', verbose_name='Usuario *', on_delete=models.PROTECT, help_text="* indica campo obrigatório.")
    data = models.DateField(_('Data da atividade física *'), help_text='Use dd/mm/aaaa')
    hora = models.TimeField(_('Hora da atividade física *'), help_text='Use hh:mm')    
    atividade = models.ForeignKey('atividade_fisica.AtividadeFisica', verbose_name="Atividade física realizada", on_delete=models.PROTECT)
    duracao = models.DecimalField(_('Quantos minutos em atividade *'), max_digits=3, decimal_places=0) 
    esforco = models.CharField(_('Esforço subjetivo *'), max_length=27, choices=BORG, help_text='Em relação ao esforço na atividade')   
    frequencia_cardiaca_media = models.DecimalField(_('Frequência cardíaca média durante a atividade'), max_digits=3, decimal_places=0, null=True, blank=True, help_text='Caso tenha utilizado um frequêncímetro durante a atividade') 
    total_calorias = models.DecimalField(max_digits=6, decimal_places=1) 
    slug = models.SlugField('Hash',max_length= 200,null=True,blank=True)

    
    class Meta:
        ordering            =   ['data', 'hora', 'atividade']
        verbose_name        =   _('registro atividade')
        verbose_name_plural =   _('registros atividades')

    def __str__(self):
         return '%s - %s - %s - %s' % (self.data, self.hora, self.atividade, self.esforco)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = gerar_hash()
        super(RegistroAtividade, self).save(*args, **kwargs)

    @property
    def get_absolute_url(self):
        return reverse('registro_atividade_update', args=[str(self.id)])

    @property
    def get_delete_url(self):
        return reverse('registro_atividade_delete', args=[str(self.id)])
