# Generated by Django 5.1.1 on 2024-09-28 07:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='big_int_val',
            field=models.BigIntegerField(default=121323),
        ),
    ]
