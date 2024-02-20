# Generated by Django 5.0.2 on 2024-02-20 15:26

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('somtuEvents', '0005_eventattendee_alter_eventdetails_event_end_date_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='BatchClass',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('class_name', models.CharField(max_length=30)),
                ('class_stream', models.CharField(max_length=20)),
                ('class_batch', models.IntegerField()),
            ],
        ),
        migrations.AlterField(
            model_name='eventdetails',
            name='event_end_date',
            field=models.DateTimeField(default=datetime.datetime(2024, 2, 20, 22, 11, 51, 415150)),
        ),
        migrations.AlterField(
            model_name='eventdetails',
            name='event_start_date',
            field=models.DateTimeField(default=datetime.datetime(2024, 2, 20, 21, 11, 51, 415150)),
        ),
    ]