# Generated by Django 3.1.5 on 2021-09-22 21:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alimento', '0002_auto_20210908_1801'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alimento',
            name='carboidratos',
            field=models.DecimalField(decimal_places=0, help_text='Quantidade de carboidratos para a unidade definida desse alimento', max_digits=5, verbose_name='Quantidade de carboidratos (g) da unidade desse alimento *'),
        ),
        migrations.AlterField(
            model_name='alimento',
            name='descricao',
            field=models.CharField(help_text='Seja sucinto na descrição do alimento. Lembre que é campo obrigatório', max_length=100, verbose_name='Descrição do alimento *'),
        ),
        migrations.AlterField(
            model_name='alimento',
            name='fonte',
            field=models.CharField(blank=True, help_text='Use como referência alguma instituição, ou artigo, ou livro, por exemplo', max_length=100, null=True, verbose_name='Fonte ou referência desse alimento'),
        ),
        migrations.AlterField(
            model_name='alimento',
            name='unidade',
            field=models.CharField(help_text='copo de 400 ml, ou colher, ou fatia, ou porção, por exemplo', max_length=100, verbose_name='Unidade do alimento *'),
        ),
    ]
