# Generated by Django 3.2.9 on 2021-11-17 04:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0003_alter_customers_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customers',
            name='image',
            field=models.FileField(upload_to='customers'),
        ),
    ]
