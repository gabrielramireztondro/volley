# Generated by Django 2.2.3 on 2019-07-22 23:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_auto_20190720_2122'),
    ]

    operations = [
        migrations.AddField(
            model_name='equipo',
            name='taller',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='main.Taller', verbose_name='Taller'),
            preserve_default=False,
        ),
    ]
