# Generated by Django 4.2.4 on 2023-08-16 18:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Solicitudes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(default='sin título', max_length=300, verbose_name='Título')),
                ('lista_desplegable', models.CharField(max_length=300, verbose_name='Tipo de solicitud')),
                ('fecha_reporte', models.DateField(default='sin editorial', max_length=300, verbose_name='Fecha del reporte')),
                ('fecha_respuesta_reporte', models.IntegerField(default=0, verbose_name='Fecha de respuesta del reporte')),
                ('descripcion', models.IntegerField(verbose_name='Descripción de la solicitud')),
                ('adjuntos', models.IntegerField(verbose_name='Archivos adjuntos')),
            ],
            options={
                'verbose_name': 'Solicitudes',
                'verbose_name_plural': 'Solicitudes',
            },
        ),
    ]