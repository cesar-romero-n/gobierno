# Generated by Django 4.2.4 on 2023-08-18 22:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('solicitudes', '0005_adjuntos_alter_solicitudes_options_respuesta_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Respuesta',
            new_name='Respuestas',
        ),
    ]
