# Generated by Django 3.2.5 on 2022-09-12 13:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('guia', '0001_initial'),
        ('argumento', '0001_initial'),
        ('call', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Telefono',
            fields=[
                ('id', models.OneToOneField(max_length=12, on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_query_name='telefono_guia', serialize=False, to='guia.guia')),
                ('tel', models.CharField(max_length=80)),
                ('fecha_call', models.DateTimeField(auto_now=True)),
                ('observacion', models.TextField(max_length=200)),
                ('estado', models.BooleanField(blank=True, default=False, null=True)),
                ('indicativo', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='call.indicativo')),
                ('motivo_call', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='motivo_call_agenda', to='argumento.motivo_call')),
            ],
        ),
        migrations.CreateModel(
            name='Informe_call',
            fields=[
                ('id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='call.telefono')),
                ('fecha', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
    ]
