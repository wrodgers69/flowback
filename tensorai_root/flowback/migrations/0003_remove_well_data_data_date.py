# Generated by Django 2.1.4 on 2019-01-07 02:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('flowback', '0002_auto_20190106_1855'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='well_data',
            name='data_date',
        ),
    ]
