# Generated by Django 3.2.9 on 2021-11-18 07:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0018_auto_20211118_1227'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='next',
            field=models.CharField(default='Read blog', max_length=125),
        ),
    ]
