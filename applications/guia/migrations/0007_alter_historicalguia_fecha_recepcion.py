# Generated by Django 3.2.5 on 2022-09-28 16:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('guia', '0006_alter_historicalguia_fecha_recepcion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historicalguia',
            name='fecha_recepcion',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Fecha gestion'),
        ),
    ]
