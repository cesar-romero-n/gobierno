# Generated by Django 4.2.4 on 2023-08-18 19:07

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('solicitudes', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='solicitudes',
            name='fecha_respuesta_reporte',
        ),
        migrations.AlterField(
            model_name='solicitudes',
            name='adjuntos',
            field=models.FileField(default=None, upload_to='adjuntos/'),
        ),
        migrations.AlterField(
            model_name='solicitudes',
            name='descripcion',
            field=models.CharField(default='Describa la solicitud a enviar', max_length=500, verbose_name='Descripción de la solicitud'),
        ),
        migrations.AlterField(
            model_name='solicitudes',
            name='fecha_reporte',
            field=models.DateField(default=datetime.datetime.today, max_length=300, verbose_name='Fecha del reporte'),
        ),
        migrations.AlterField(
            model_name='solicitudes',
            name='lista_desplegable',
            field=models.CharField(choices=[('Reporte de problema', 'Reporte de problema'), ('Solicitud de información', 'Solicitud de información')], default='Reporte de problema', max_length=50, verbose_name='Tipo de solicitud'),
        ),
        migrations.AlterField(
            model_name='solicitudes',
            name='titulo',
            field=models.CharField(default='Título de la solicitud a levantar', max_length=300, verbose_name='Título'),
        ),
    ]
