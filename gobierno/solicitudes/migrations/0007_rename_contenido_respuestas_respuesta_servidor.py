# Generated by Django 4.2.4 on 2023-08-18 22:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('solicitudes', '0006_rename_respuesta_respuestas'),
    ]

    operations = [
        migrations.RenameField(
            model_name='respuestas',
            old_name='contenido',
            new_name='respuesta_servidor',
        ),
    ]
