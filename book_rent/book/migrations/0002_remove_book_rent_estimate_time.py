# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-18 16:42
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='rent_estimate_time',
        ),
    ]
