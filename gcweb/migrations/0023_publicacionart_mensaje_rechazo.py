# Generated by Django 4.2.1 on 2023-06-26 18:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gcweb', '0022_remove_datos_artista_usuario_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='publicacionart',
            name='mensaje_rechazo',
            field=models.TextField(default='nada', max_length=200),
            preserve_default=False,
        ),
    ]
