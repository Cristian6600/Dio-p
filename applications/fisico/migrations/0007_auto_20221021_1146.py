# Generated by Django 3.2.5 on 2022-10-21 16:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fisico', '0006_auto_20220928_1132'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fisico',
            name='estado',
        ),
        migrations.RemoveField(
            model_name='fisico',
            name='fecha',
        ),
        migrations.AddField(
            model_name='bolsa',
            name='estado',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='bolsa',
            name='fecha',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='Fecha fisico'),
        ),
    ]
