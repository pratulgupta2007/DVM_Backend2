# Generated by Django 5.1.2 on 2024-11-22 14:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_rename_tp_created_at_otptoken_otp_created_at_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='otptoken',
            name='otp_code',
            field=models.CharField(default=' ', max_length=6),
        ),
    ]