# Generated by Django 5.1.2 on 2024-11-02 16:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0016_alter_tickets_total'),
    ]

    operations = [
        migrations.AddField(
            model_name='tickets',
            name='verified',
            field=models.BooleanField(default=0),
        ),
    ]
