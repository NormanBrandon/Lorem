# Generated by Django 2.0.4 on 2018-05-14 08:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0003_auto_20180512_0142'),
    ]

    operations = [
        migrations.AddField(
            model_name='buy',
            name='selected',
            field=models.BooleanField(default='False', verbose_name='Seleccionado'),
        ),
    ]
