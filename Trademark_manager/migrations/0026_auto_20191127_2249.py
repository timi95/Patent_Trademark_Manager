# Generated by Django 2.2.2 on 2019-11-27 22:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Trademark_manager', '0025_auto_20191127_2245'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile_actions_relative',
            name='action1',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Trademark_manager.TrademarkAction1'),
        ),
        migrations.AddField(
            model_name='profile_actions_relative',
            name='action2',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Trademark_manager.TrademarkAction2'),
        ),
        migrations.AddField(
            model_name='profile_actions_relative',
            name='profile',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='trademark_profile', to='Trademark_manager.TrademarkProfile'),
        ),
    ]
