# Generated by Django 3.2.5 on 2022-09-12 13:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('guia', '0001_initial'),
        ('argumento', '0001_initial'),
        ('call', '0002_informe_call_telefono'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='telefono',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Usuario call'),
        ),
        migrations.AddField(
            model_name='historicaldatos_t',
            name='history_user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='historicaldatos_t',
            name='telefono',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='call.telefono'),
        ),
        migrations.AddField(
            model_name='historicaldatos_t',
            name='user',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to=settings.AUTH_USER_MODEL, verbose_name='Usuario'),
        ),
        migrations.AddField(
            model_name='datos_t',
            name='telefono',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='call.telefono'),
        ),
        migrations.AddField(
            model_name='datos_t',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Usuario'),
        ),
        migrations.AddField(
            model_name='auditoria',
            name='calificacion_1',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='calificacion_1', to='call.calificacion'),
        ),
        migrations.AddField(
            model_name='auditoria',
            name='calificacion_2',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='calificacion_2', to='call.calificacion'),
        ),
        migrations.AddField(
            model_name='auditoria',
            name='calificacion_3',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='calificacion_3', to='call.calificacion'),
        ),
        migrations.AddField(
            model_name='auditoria',
            name='calificacion_4',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='calificacion_4', to='call.calificacion'),
        ),
        migrations.AddField(
            model_name='auditoria',
            name='entregas',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='guia.guia'),
        ),
        migrations.AddField(
            model_name='auditoria',
            name='motivo_call',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='argumento.motivo_call'),
        ),
        migrations.AddField(
            model_name='auditoria',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Usuario'),
        ),
    ]
