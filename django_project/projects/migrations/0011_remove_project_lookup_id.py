# Generated by Django 3.1.2 on 2020-11-12 03:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0010_project_lookup_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='lookup_id',
        ),
    ]
