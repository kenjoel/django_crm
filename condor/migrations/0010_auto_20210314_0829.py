# Generated by Django 3.1.5 on 2021-03-14 08:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('condor', '0009_condor_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='condor',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='clients', to='condor.category'),
        ),
    ]