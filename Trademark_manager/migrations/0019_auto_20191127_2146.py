# Generated by Django 2.2.2 on 2019-11-27 21:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Trademark_manager', '0018_auto_20191127_0748'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile_actions_relative',
            name='action1',
        ),
        migrations.RemoveField(
            model_name='profile_actions_relative',
            name='action2',
        ),
        migrations.RemoveField(
            model_name='profile_actions_relative',
            name='profile',
        ),
        migrations.AddField(
            model_name='trademarkprofile',
            name='action1',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='action1', to='Trademark_manager.TrademarkAction1'),
        ),
    ]
