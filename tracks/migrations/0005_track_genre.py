# Generated by Django 2.2.3 on 2019-10-26 23:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracks', '0004_like_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='track',
            name='genre',
            field=models.CharField(default='', max_length=30),
        ),
    ]
