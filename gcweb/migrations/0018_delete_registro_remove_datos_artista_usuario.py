# Generated by Django 4.2.1 on 2023-06-25 21:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gcweb', '0017_publicacionart_estado'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Registro',
        ),
        migrations.RemoveField(
            model_name='datos_artista',
            name='usuario',
        ),
    ]
