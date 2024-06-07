from __future__ import unicode_literals

from django.conf import settings
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _

from utils.gerador_hash import gerar_hash


class RegistroRefeicao(models.Model):
    #1 campo da tupla fica no banco de dados
    #2 campo da tupla eh mostrado para o usuario
    TIPO_REFEICAO = (
        ('CAFÉ DA MANHÃ', 'Café da manhã'),
        ('ALMOÇO', 'Almoço'),
        ('LANCHE', 'Lanche' ),
        ('JANTAR', 'Jantar'),
        ('REFEIÇÃO EXTRA', 'Refeição extra' ),
    )
    cliente = models.ForeignKey('usuario.Usuario', verbose_name='Usuario *', on_delete=models.PROTECT, help_text="* indica campo obrigatório.")
    data = models.DateField(_('Data de consumo do alimento *'), help_text='Use dd/mm/aaaa')
    hora = models.TimeField(_('Hora de consumo do alimento *'), help_text='Use hh:mm')
    alimento = models.ForeignKey('alimento.Alimento', verbose_name="Alimento", on_delete=models.PROTECT, help_text="* indica campo obrigatório.")
    quantidade = models.DecimalField(_('Quantidade do alimento *'), max_digits=3, decimal_places=1, help_text='Utilize 0.5 para meia porção') 
    total_carboidratos = models.DecimalField(max_digits=6, decimal_places=1) 
    total_calorias = models.DecimalField(max_digits=6, decimal_places=1) 
    slug = models.SlugField('Hash',max_length= 200,null=True,blank=True)

    
    class Meta:
        ordering            =   ['cliente','data', 'hora', 'alimento']
        verbose_name        =   _('registro_refeicao')
        verbose_name_plural =   _('registros_refeicoes')

    def __str__(self):
         return '%s - %s - %s - %s - %s' % (self.cliente, self.data, self.hora, self.alimento, self.quantidade)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = gerar_hash()
        super(RegistroRefeicao, self).save(*args, **kwargs)

    @property
    def get_absolute_url(self):
        return reverse('registro_refeicao_update', args=[str(self.id)])

    @property
    def get_delete_url(self):
        return reverse('registro_refeicao_delete', args=[str(self.id)])
