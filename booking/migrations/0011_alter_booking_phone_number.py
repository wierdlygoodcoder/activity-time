# Generated by Django 3.2.16 on 2022-10-16 14:38

from django.db import migrations
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0010_auto_20221016_1437'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='phone_number',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, region='GB'),
        ),
    ]