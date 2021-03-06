# Generated by Django 2.2.2 on 2019-11-25 18:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Trademark_manager', '0011_auto_20191123_1159'),
    ]

    operations = [
        migrations.CreateModel(
            name='TrademarkAction1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='TrademarkAction2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='TrademarkParticulars',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='TrademarkProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client_name', models.CharField(default='default client name', max_length=50)),
                ('trademark_particulars', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='Trademark_manager.TrademarkParticulars')),
            ],
        ),
    ]
