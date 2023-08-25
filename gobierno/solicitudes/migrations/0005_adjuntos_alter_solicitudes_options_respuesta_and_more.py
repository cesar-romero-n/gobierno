# Generated by Django 4.2.4 on 2023-08-18 22:00

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('solicitudes', '0004_alter_solicitudes_options_alter_solicitudes_adjuntos_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Adjuntos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('archivo', models.FileField(null=True, upload_to='adjuntos/')),
            ],
        ),
        migrations.AlterModelOptions(
            name='solicitudes',
            options={'verbose_name': 'Solicitud', 'verbose_name_plural': 'Solicitud'},
        ),
        migrations.CreateModel(
            name='Respuesta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_respuesta', models.DateField(default=datetime.datetime.today, verbose_name='Fecha de respuesta')),
                ('contenido', models.TextField(verbose_name='Contenido de la respuesta')),
                ('solicitud', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='solicitudes.solicitudes')),
            ],
        ),
        migrations.AlterField(
            model_name='solicitudes',
            name='adjuntos',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='solicitudes.adjuntos'),
        ),
    ]