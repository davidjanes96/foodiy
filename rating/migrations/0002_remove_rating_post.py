# Generated by Django 3.1.4 on 2021-01-08 14:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rating', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rating',
            name='post',
        ),
    ]
