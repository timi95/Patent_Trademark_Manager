# Generated by Django 2.2.2 on 2019-11-26 06:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Trademark_manager', '0015_auto_20191126_0646'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trademarkaction1',
            name='profile',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Trademark_manager.TrademarkProfile'),
        ),
        migrations.AlterField(
            model_name='trademarkaction2',
            name='profile',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Trademark_manager.TrademarkProfile'),
        ),
    ]
