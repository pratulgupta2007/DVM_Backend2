# Generated by Django 5.1.2 on 2024-11-01 09:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0011_alter_wallet_balance'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='wallet',
            name='transaction',
        ),
    ]
