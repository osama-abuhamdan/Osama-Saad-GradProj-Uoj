# Generated by Django 3.0.3 on 2020-04-22 23:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('search_title', '0015_auto_20200421_2250'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='title',
            name='job_done',
        ),
        migrations.AddField(
            model_name='job',
            name='job_done',
            field=models.BooleanField(default=0),
            preserve_default=False,
        ),
    ]