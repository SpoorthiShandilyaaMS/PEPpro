# Generated by Django 3.1.1 on 2020-11-05 11:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PEPapp', '0010_auto_20201105_1106'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news_feed',
            name='feed_date',
            field=models.DateField(auto_now=True, null=True),
        ),
    ]