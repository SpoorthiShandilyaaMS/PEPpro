# Generated by Django 3.1.1 on 2020-11-02 11:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('PEPapp', '0004_news_feed_sector'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sector',
            old_name='sector',
            new_name='sector_id',
        ),
    ]