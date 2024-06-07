# Generated by Django 3.1.5 on 2021-09-01 21:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AtividadeFisica',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(help_text='* Campos obrigatórios', max_length=25, unique=True, verbose_name='Nome da atividade *')),
                ('descricao', models.TextField(blank=True, help_text='Se necessário, explique a atividade física', max_length=1000, null=True, verbose_name='Detalhes da atividade física')),
                ('tipo', models.CharField(choices=[('AERÓBICA', 'Aeróbica'), ('ANAERÓBICA', 'Anaeróbica'), ('ALONGAMENTO', 'Alongamento')], help_text='Em relação ao consumo de oxigênio', max_length=15, verbose_name='Tipo de atividade *')),
                ('slug', models.SlugField(blank=True, max_length=200, null=True, verbose_name='Hash')),
            ],
            options={
                'verbose_name': 'atividade_fisica',
                'verbose_name_plural': 'atividades_fisicas',
                'ordering': ['nome'],
            },
        ),
    ]
