# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-17 11:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('robot', '0005_auto_20170423_2105'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customize',
            name='loops',
        ),
        migrations.AddField(
            model_name='customize',
            name='music',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='motion',
            name='order',
            field=models.IntegerField(default=1000),
        ),
    ]