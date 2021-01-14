# Generated by Django 3.1.4 on 2021-01-08 19:03

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rating', '0003_auto_20210108_1819'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rating',
            name='score',
            field=models.PositiveSmallIntegerField(null=True, validators=[django.core.validators.MaxValueValidator(5), django.core.validators.MinValueValidator(0)]),
        ),
    ]
