# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2019-08-22 06:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ServicesData',
            fields=[
                ('course_id', models.IntegerField(primary_key=True, serialize=False)),
                ('course_name', models.CharField(max_length=100, unique=True)),
                ('course_duration', models.CharField(max_length=100)),
                ('course_state_date', models.DateField(max_length=100)),
                ('course_start_time', models.TextField(max_length=100)),
                ('course_trainer_name', models.CharField(max_length=100)),
                ('course_trainer_exp', models.CharField(max_length=100)),
            ],
        ),
    ]
