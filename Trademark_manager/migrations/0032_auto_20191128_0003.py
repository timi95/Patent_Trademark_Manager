# Generated by Django 2.2.2 on 2019-11-28 00:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Trademark_manager', '0031_auto_20191127_2321'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='trademarkprofile',
            name='action1',
        ),
        migrations.RemoveField(
            model_name='trademarkprofile',
            name='action2',
        ),
    ]