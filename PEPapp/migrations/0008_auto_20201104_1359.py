# Generated by Django 3.1.1 on 2020-11-04 08:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PEPapp', '0007_auto_20201104_1351'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='umobile',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]