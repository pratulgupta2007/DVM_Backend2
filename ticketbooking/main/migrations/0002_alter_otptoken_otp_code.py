# Generated by Django 5.1.2 on 2024-11-12 16:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='otptoken',
            name='otp_code',
            field=models.CharField(default='7ea7c6', max_length=6),
        ),
    ]
