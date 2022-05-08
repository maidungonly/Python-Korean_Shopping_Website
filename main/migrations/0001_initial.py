# Generated by Django 3.2.13 on 2022-05-08 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='KcookPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_post', models.TextField()),
                ('image', models.ImageField(upload_to='kcookpost_imgs/')),
                ('nguyenlieu', models.TextField()),
                ('introduction', models.CharField(max_length=350, null=True)),
                ('cachlam', models.TextField()),
                ('slug', models.SlugField(blank=True, unique=True)),
            ],
        ),
    ]
