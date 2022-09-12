# Generated by Django 3.2.5 on 2022-09-12 13:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ciudad',
            fields=[
                ('id', models.CharField(max_length=10, primary_key=True, serialize=False, unique=True, verbose_name='Dane')),
                ('ciudad', models.CharField(max_length=80)),
                ('cubrimiento', models.CharField(blank=True, max_length=15, null=True)),
            ],
            options={
                'ordering': ['ciudad'],
            },
        ),
        migrations.CreateModel(
            name='Departamento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('departamento', models.CharField(max_length=30)),
                ('capital', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Oficinas',
            fields=[
                ('id', models.CharField(max_length=6, primary_key=True, serialize=False)),
                ('nom_ofi', models.CharField(max_length=80)),
                ('direccion', models.CharField(max_length=200)),
                ('hora_norm', models.CharField(max_length=90, verbose_name='Horario normal')),
                ('hora_adi', models.CharField(max_length=90, verbose_name='Horario adicional')),
                ('hora_sab', models.CharField(max_length=90, verbose_name='Horario sabado')),
                ('categoria', models.CharField(max_length=20)),
                ('num_dia_entr', models.CharField(max_length=8, verbose_name='N° Días Entrega_(hábiles)')),
                ('lunes', models.CharField(max_length=3)),
                ('martes', models.CharField(max_length=3)),
                ('miercoles', models.CharField(max_length=3)),
                ('jueves', models.CharField(max_length=3)),
                ('viernes', models.CharField(max_length=3)),
                ('sabado', models.CharField(max_length=3)),
                ('fusionada', models.CharField(blank=True, max_length=60, null=True)),
                ('observacion', models.TextField()),
                ('fecha_actu', models.DateField(verbose_name='Fecha ultima actualizacion')),
                ('dir_cita', models.CharField(max_length=150, verbose_name='Direccion cita')),
                ('cub', models.CharField(max_length=16)),
                ('dane', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cliente.ciudad')),
            ],
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id_clie', models.CharField(max_length=10, primary_key=True, serialize=False, verbose_name='Id cliente')),
                ('nit', models.CharField(max_length=20)),
                ('r_s', models.CharField(max_length=70, verbose_name='Razon social')),
                ('contact', models.CharField(max_length=50, verbose_name='Contacto')),
                ('dir', models.CharField(max_length=120, verbose_name='Direccion')),
                ('tel', models.IntegerField(verbose_name='Tel fijo')),
                ('cel', models.IntegerField(verbose_name='Celular')),
                ('radicacion', models.IntegerField()),
                ('fact', models.CharField(max_length=4, verbose_name='Factura')),
                ('id_ciu', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cliente.ciudad', verbose_name='Id ciudad')),
            ],
            options={
                'verbose_name': 'Cliente',
                'verbose_name_plural': 'Cliente',
            },
        ),
        migrations.AddField(
            model_name='ciudad',
            name='departamento',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cliente.departamento', verbose_name='departamento_ciudad'),
        ),
    ]
