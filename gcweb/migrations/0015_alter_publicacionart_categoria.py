# Generated by Django 4.2.1 on 2023-06-23 23:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gcweb', '0014_categoria_remove_datos_artista_edad_artista_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publicacionart',
            name='categoria',
            field=models.ForeignKey(choices=[[0, 'Pintor'], [1, 'Escultor']], null=True, on_delete=django.db.models.deletion.PROTECT, to='gcweb.categoria'),
        ),
    ]
