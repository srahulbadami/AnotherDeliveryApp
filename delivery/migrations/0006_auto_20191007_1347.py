# Generated by Django 2.2.6 on 2019-10-07 13:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('delivery', '0005_delivery_agent_suit_length'),
    ]

    operations = [
        migrations.RenameField(
            model_name='delivery_agent',
            old_name='suit_length',
            new_name='total_distance',
        ),
    ]