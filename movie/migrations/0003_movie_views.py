# Generated by Django 4.2.5 on 2024-04-12 07:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0002_favorite'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='views',
            field=models.IntegerField(default=0),
        ),
    ]
