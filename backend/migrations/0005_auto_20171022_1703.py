# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-22 17:03
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0004_auto_20171022_0405'),
    ]

    operations = [
        migrations.CreateModel(
            name='DanceRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('x_speed', models.FloatField()),
                ('y_speed', models.FloatField()),
                ('z_speed', models.FloatField()),
                ('time', models.IntegerField()),
            ],
        ),
        migrations.RemoveField(
            model_name='dance',
            name='records',
        ),
        migrations.AddField(
            model_name='dance',
            name='name',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='dancerecord',
            name='dance',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.Dance'),
        ),
    ]
