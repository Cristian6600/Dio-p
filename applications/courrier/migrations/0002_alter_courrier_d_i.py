# Generated by Django 3.2.5 on 2022-09-16 16:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courrier', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='courrier',
            name='d_i',
            field=models.CharField(max_length=12, unique=True, verbose_name='Documento identidad'),
        ),
    ]
