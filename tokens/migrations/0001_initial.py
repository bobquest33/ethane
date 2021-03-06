# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-14 18:15
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Token',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('public_name', models.CharField(max_length=200)),
                ('symbol', models.CharField(max_length=4)),
                ('decimals', models.IntegerField(default=18, validators=[django.core.validators.MaxValueValidator(20), django.core.validators.MinValueValidator(0)])),
                ('phase', models.CharField(choices=[('PHASE_01', 'In review'), ('PHASE_02', 'Active'), ('PHASE_02', 'Inactive')], default='PHASE_01', max_length=8)),
            ],
        ),
    ]
