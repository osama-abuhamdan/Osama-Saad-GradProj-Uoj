# Generated by Django 3.0.3 on 2020-03-18 14:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('search_title', '0006_auto_20200318_1435'),
    ]

    operations = [
        migrations.AlterField(
            model_name='title',
            name='poster',
            field=models.TextField(),
        ),
    ]
