# Generated by Django 5.0.2 on 2024-02-20 16:04

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('somtuEvents', '0006_batchclass_alter_eventdetails_event_end_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eventdetails',
            name='event_end_date',
            field=models.DateTimeField(default=datetime.datetime(2024, 2, 20, 22, 49, 51, 572472)),
        ),
        migrations.AlterField(
            model_name='eventdetails',
            name='event_start_date',
            field=models.DateTimeField(default=datetime.datetime(2024, 2, 20, 21, 49, 51, 572472)),
        ),
    ]
