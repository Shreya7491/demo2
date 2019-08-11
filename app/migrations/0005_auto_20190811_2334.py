# Generated by Django 2.0.7 on 2019-08-11 18:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_auto_20190810_1133'),
    ]

    operations = [
        migrations.CreateModel(
            name='Random',
            fields=[
                ('random_no', models.CharField(max_length=255, primary_key=True, serialize=False)),
            ],
        ),
        migrations.AddField(
            model_name='show',
            name='random_string',
            field=models.OneToOneField(default='singh', on_delete=django.db.models.deletion.CASCADE, to='app.Random'),
        ),
    ]
