# Generated by Django 4.2.1 on 2023-06-24 00:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gcweb', '0016_alter_publicacionart_categoria'),
    ]

    operations = [
        migrations.AddField(
            model_name='publicacionart',
            name='estado',
            field=models.IntegerField(choices=[[0, 'En Espera'], [1, 'Aprobado'], [2, 'Rechazado']], default=0),
        ),
    ]