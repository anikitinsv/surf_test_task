# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-18 18:00
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0002_remove_book_rent_estimate_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='count_month_rented',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='book',
            name='rent_estimate_time',
            field=models.DateTimeField(default=datetime.datetime(2017, 6, 18, 18, 0, 14, 607061)),
        ),
    ]
