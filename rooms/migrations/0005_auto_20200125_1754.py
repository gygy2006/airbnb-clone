# Generated by Django 2.2.5 on 2020-01-25 08:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rooms', '0004_auto_20200125_1246'),
    ]

    operations = [
        migrations.RenameField(
            model_name='room',
            old_name='adress',
            new_name='address',
        ),
    ]
