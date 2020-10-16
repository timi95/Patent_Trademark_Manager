# Generated by Django 2.1.11 on 2020-10-16 21:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Reminder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='default value', max_length=50)),
                ('reminder_detail', models.TextField()),
                ('reminder_date', models.DateTimeField()),
                ('manager_type', models.CharField(default='default value', max_length=50)),
                ('document_type', models.CharField(default='default value', max_length=50)),
                ('document_id', models.CharField(default='default value', max_length=50)),
            ],
        ),
    ]
