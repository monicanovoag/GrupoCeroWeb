# Generated by Django 4.2.1 on 2023-06-04 05:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gcweb', '0002_datos_artista_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='datos_artista',
            old_name='tipo_Artista',
            new_name='especialidad',
        ),
    ]
