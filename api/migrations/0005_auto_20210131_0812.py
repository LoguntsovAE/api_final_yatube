# Generated by Django 3.1.5 on 2021-01-31 08:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_auto_20210131_0801'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='group',
            name='description',
        ),
        migrations.RemoveField(
            model_name='group',
            name='slug',
        ),
    ]
