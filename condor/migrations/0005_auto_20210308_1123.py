# Generated by Django 3.1.5 on 2021-03-08 11:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('condor', '0004_category_organisation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='organisation',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='condor.userprofile'),
        ),
    ]
