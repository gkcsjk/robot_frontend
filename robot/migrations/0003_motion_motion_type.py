# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-23 04:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('robot', '0002_auto_20170421_1517'),
    ]

    operations = [
        migrations.AddField(
            model_name='motion',
            name='motion_type',
            field=models.CharField(default='default motion', max_length=50),
        ),
    ]