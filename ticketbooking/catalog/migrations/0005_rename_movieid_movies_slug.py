# Generated by Django 5.1.2 on 2024-10-24 13:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0004_alter_movies_movieid'),
    ]

    operations = [
        migrations.RenameField(
            model_name='movies',
            old_name='movieID',
            new_name='slug',
        ),
    ]
