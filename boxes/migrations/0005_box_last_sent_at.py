# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-15 14:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boxes', '0004_auto_20160415_1428'),
    ]

    operations = [
        migrations.AddField(
            model_name='box',
            name='last_sent_at',
            field=models.DateTimeField(null=True),
        ),
    ]
