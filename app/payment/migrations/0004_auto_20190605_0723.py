# Generated by Django 2.2 on 2019-06-05 07:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0003_auto_20190603_0749'),
    ]

    operations = [
        migrations.AddField(
            model_name='transactioncounterpay',
            name='counter_transaction_no',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='guesttemporaryinfo',
            name='id',
            field=models.CharField(default='3c513e00', max_length=255, primary_key=True, serialize=False, unique=True),
        ),
    ]