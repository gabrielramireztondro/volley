# Generated by Django 2.2.3 on 2019-07-29 01:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_auto_20190729_0115'),
    ]

    operations = [
        migrations.AddField(
            model_name='persona',
            name='es_diestro',
            field=models.BooleanField(default=True),
        ),
    ]
