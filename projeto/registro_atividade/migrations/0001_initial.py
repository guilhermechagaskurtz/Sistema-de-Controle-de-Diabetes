# Generated by Django 3.1.5 on 2021-11-03 22:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('atividade_fisica', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='RegistroAtividade',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DateField(help_text='Use dd/mm/aaaa', verbose_name='Data da atividade física *')),
                ('hora', models.TimeField(help_text='Use hh:mm', verbose_name='Hora da atividade física *')),
                ('duracao', models.DecimalField(decimal_places=0, max_digits=3, verbose_name='Quantos minutos em atividade *')),
                ('esforco', models.CharField(choices=[('7', 'Muito fácil'), ('9', 'Fácil'), ('11', 'Relativamente fácil'), ('13', 'Ligeiramente cansativo'), ('15', 'Cansativo'), ('17', 'Muito cansativo'), ('19', 'Exaustivo')], help_text='Em relação ao esforço na atividade', max_length=22, verbose_name='Esforço subjetivo *')),
                ('frequencia_cardiaca_media', models.DecimalField(decimal_places=0, help_text='Caso tenha utilizado um frequêncímetro durante a atividade', max_digits=3, verbose_name='Frequência cardíaca média durante a atividade')),
                ('total_calorias', models.DecimalField(decimal_places=1, max_digits=6)),
                ('slug', models.SlugField(blank=True, max_length=200, null=True, verbose_name='Hash')),
                ('atividade', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='atividade_fisica.atividadefisica', verbose_name='Atividade física realizada')),
            ],
            options={
                'verbose_name': 'registro atividade',
                'verbose_name_plural': 'registros atividades',
                'ordering': ['data', 'hora', 'atividade'],
            },
        ),
    ]
