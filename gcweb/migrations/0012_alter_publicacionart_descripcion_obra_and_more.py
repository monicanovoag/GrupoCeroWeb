# Generated by Django 4.2.1 on 2023-06-08 17:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gcweb', '0011_rename_apellido_registro_registro_apellido_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publicacionart',
            name='descripcion_obra',
            field=models.TextField(max_length=200),
        ),
        migrations.AlterField(
            model_name='publicacionart',
            name='imagen_obra',
            field=models.ImageField(null=True, upload_to='obras'),
        ),
    ]
