# Generated by Django 3.2.9 on 2021-11-17 11:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0009_auto_20211117_1628'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='image',
            field=models.FileField(upload_to='reviews'),
        ),
    ]
