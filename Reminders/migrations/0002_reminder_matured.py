# Generated by Django 2.1.11 on 2020-10-20 16:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Reminders', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='reminder',
            name='matured',
            field=models.BooleanField(default=False),
        ),
    ]