# Generated by Django 3.2.5 on 2022-09-26 17:27

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('guia', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historicalguia',
            name='fecha_recepcion',
            field=models.DateTimeField(blank=True, db_index=True, default=django.utils.timezone.now, null=True, verbose_name='Fecha gestion'),
        ),
    ]
