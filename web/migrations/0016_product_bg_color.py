# Generated by Django 3.2.9 on 2021-11-18 06:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0015_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='bg_color',
            field=models.CharField(default='#fff', max_length=10),
        ),
    ]
