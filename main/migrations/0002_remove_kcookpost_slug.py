# Generated by Django 3.2.13 on 2022-05-08 15:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='kcookpost',
            name='slug',
        ),
    ]
