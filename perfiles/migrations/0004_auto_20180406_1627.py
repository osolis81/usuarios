# Generated by Django 2.0.3 on 2018-04-06 16:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('perfiles', '0003_auto_20180325_2356'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='carreras',
            name='id_campus',
        ),
        migrations.AddField(
            model_name='asignaturasresumen',
            name='id_campus',
            field=models.ForeignKey(default=1.0, on_delete=django.db.models.deletion.CASCADE, to='perfiles.campus'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='estudiantesresumen',
            name='id_campus',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, to='perfiles.campus'),
            preserve_default=False,
        ),
    ]