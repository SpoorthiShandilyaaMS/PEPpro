# Generated by Django 3.1.1 on 2020-11-02 12:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('PEPapp', '0005_auto_20201102_1700'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='usertype',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='news_feed',
            name='feed_date',
            field=models.DateField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='news_feed',
            name='feed_description',
            field=models.CharField(max_length=400),
        ),
        migrations.AlterField(
            model_name='news_feed',
            name='feed_title',
            field=models.CharField(max_length=50),
        ),
        migrations.CreateModel(
            name='Query',
            fields=[
                ('query_id', models.IntegerField(primary_key=True, serialize=False)),
                ('query', models.CharField(max_length=100)),
                ('date', models.DateField(auto_now=True)),
                ('posted_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='PEPapp.user')),
            ],
        ),
        migrations.CreateModel(
            name='Complaint',
            fields=[
                ('complaint_id', models.IntegerField(primary_key=True, serialize=False)),
                ('complaint_subject', models.CharField(max_length=50)),
                ('complaint_details', models.CharField(max_length=300)),
                ('no_up_vote', models.IntegerField()),
                ('upvoted_by', models.CharField(max_length=50, null=True)),
                ('constituency_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='PEPapp.constituency')),
                ('posted_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='PEPapp.user')),
                ('sector_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='PEPapp.sector')),
            ],
        ),
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('answer_id', models.IntegerField(primary_key=True, serialize=False)),
                ('answer', models.CharField(max_length=200)),
                ('date', models.DateField(auto_now=True)),
                ('query_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='PEPapp.query')),
                ('user_email', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='PEPapp.user')),
            ],
        ),
    ]