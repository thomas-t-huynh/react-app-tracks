# Generated by Django 2.2.3 on 2019-11-29 17:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tracks', '0007_auto_20191126_2044'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='user',
            new_name='posted_by',
        ),
    ]