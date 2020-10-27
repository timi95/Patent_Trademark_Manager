# Generated by Django 2.1.11 on 2020-10-03 08:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Trademark_manager', '0045_trademarkprofile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='certificateprocurementaction',
            name='journal_no',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='certificateprocurementaction',
            name='journal_vol',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='certificateprocurementaction',
            name='registration_no',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='registrationaction',
            name='trademark_class',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='trademarkprofile',
            name='applicable_official_fee',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=12, null=True),
        ),
        migrations.AlterField(
            model_name='trademarkprofile',
            name='applicable_service_charge',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=12, null=True),
        ),
        migrations.AlterField(
            model_name='trademarkprofile',
            name='incentive_due_clerk',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='trademarkprofile',
            name='quicktellers_fee',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=12, null=True),
        ),
        migrations.AlterField(
            model_name='trademarkprofile',
            name='registration_no',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='trademarkprofile',
            name='trademark_class',
            field=models.IntegerField(),
        ),
    ]