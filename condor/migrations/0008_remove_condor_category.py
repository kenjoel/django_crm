# Generated by Django 3.1.5 on 2021-03-14 05:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('condor', '0007_auto_20210314_0451'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='condor',
            name='category',
        ),
    ]