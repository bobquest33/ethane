# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-22 19:54
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tokens', '0008_auto_20170722_1932'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='token',
            name='token_type',
        ),
    ]
