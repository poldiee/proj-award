# Generated by Django 4.0.5 on 2022-06-16 23:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myawards', '0005_rating'),
    ]

    operations = [
        migrations.RenameField(
            model_name='rating',
            old_name='post_rated',
            new_name='post',
        ),
    ]