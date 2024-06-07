# Generated by Django 3.1.5 on 2021-10-13 21:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('alimento', '0003_auto_20210922_1835'),
    ]

    operations = [
        migrations.CreateModel(
            name='RegistroRefeicao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DateField(help_text='Use dd/mm/aaaa', verbose_name='Data de consumo do alimento *')),
                ('hora', models.TimeField(help_text='Use hh:mm', verbose_name='Hora de consumo do alimento *')),
                ('quantidade', models.DecimalField(decimal_places=1, help_text='Utilize 0.5 para meia porção', max_digits=3, verbose_name='Quantidade do alimento *')),
                ('slug', models.SlugField(blank=True, max_length=200, null=True, verbose_name='Hash')),
                ('alimento', models.ForeignKey(help_text='* indica campo obrigatório.', on_delete=django.db.models.deletion.PROTECT, to='alimento.alimento', verbose_name='Alimento')),
            ],
            options={
                'verbose_name': 'registro_refeicao',
                'verbose_name_plural': 'registros_refeicoes',
                'ordering': ['data', 'hora', 'alimento'],
            },
        ),
    ]