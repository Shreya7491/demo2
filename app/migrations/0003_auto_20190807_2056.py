# Generated by Django 2.0.7 on 2019-08-07 15:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20190807_2009'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='question',
            field=models.TextField(max_length=1000, unique=True),
        ),
    ]
