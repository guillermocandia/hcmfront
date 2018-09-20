# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-09-20 22:25
from __future__ import unicode_literals

import app.working_day.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dayOfTheWeek', app.working_day.models.DayOfTheWeekField(choices=[(b'1', 'Monday'), (b'2', 'Tuesday'), (b'3', 'Wednesday'), (b'4', 'Thursday'), (b'5', 'Friday'), (b'6', 'Saturday'), (b'7', 'Sunday')], max_length=1)),
                ('start', models.TimeField(verbose_name=b'Start')),
                ('end', models.TimeField(verbose_name=b'End')),
                ('active', models.BooleanField(default=True, verbose_name=b'Active')),
            ],
            options={
                'verbose_name': 'Schedule',
                'verbose_name_plural': 'Schedules',
            },
        ),
        migrations.CreateModel(
            name='WorkingDay',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, unique=True, verbose_name=b'Name')),
                ('code', models.CharField(max_length=8, verbose_name=b'Code')),
                ('active', models.BooleanField(default=True, verbose_name=b'Active')),
            ],
            options={
                'verbose_name': 'Working Day',
                'verbose_name_plural': 'Working Days',
            },
        ),
        migrations.AddField(
            model_name='schedule',
            name='working_day',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='working_day.WorkingDay'),
        ),
    ]