# Generated by Django 3.0.4 on 2020-03-25 21:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meuapp', '0004_endereco_linguagens_pessoa'),
    ]

    operations = [
        migrations.AddField(
            model_name='pessoa',
            name='cpd',
            field=models.CharField(default='00000000000', max_length=11),
        ),
    ]