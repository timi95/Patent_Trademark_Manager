# Generated by Django 2.2.2 on 2019-11-26 06:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Trademark_manager', '0014_auto_20191126_0638'),
    ]

    operations = [
        migrations.AddField(
            model_name='trademarkaction1',
            name='action_name',
            field=models.CharField(default='default action', max_length=50),
        ),
        migrations.AddField(
            model_name='trademarkaction2',
            name='action_name',
            field=models.CharField(default='default action', max_length=50),
        ),
    ]