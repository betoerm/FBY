# Generated by Django 3.0.4 on 2020-04-06 22:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('meuapp', '0005_pessoa_cpd'),
    ]

    operations = [
        migrations.AddField(
            model_name='pessoa',
            name='endereco',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='meuapp.Endereco'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pessoa',
            name='numero',
            field=models.IntegerField(default=1),
        ),
    ]
