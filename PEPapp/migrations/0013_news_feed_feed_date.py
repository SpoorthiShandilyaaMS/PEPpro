# Generated by Django 3.1.1 on 2020-11-05 11:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PEPapp', '0012_remove_news_feed_feed_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='news_feed',
            name='feed_date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
