# Generated by Django 3.1.2 on 2020-10-27 01:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0003_auto_20201019_0359'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='image',
            field=models.ImageField(default='default-project.jpg', upload_to='projects'),
        ),
    ]
