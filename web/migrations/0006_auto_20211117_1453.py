# Generated by Django 3.2.9 on 2021-11-17 09:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0005_feature'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feature',
            name='description',
            field=models.TextField(max_length=25),
        ),
        migrations.AlterField(
            model_name='feature',
            name='title',
            field=models.CharField(max_length=25),
        ),
    ]