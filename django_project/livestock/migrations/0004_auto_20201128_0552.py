# Generated by Django 3.1.2 on 2020-11-28 05:52

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('livestock', '0003_auto_20201128_0546'),
    ]

    operations = [
        migrations.AlterField(
            model_name='animallog',
            name='date',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]
