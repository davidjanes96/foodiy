# Generated by Django 3.1.4 on 2020-12-28 17:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20201228_1750'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpostingredient',
            name='ingredient',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
