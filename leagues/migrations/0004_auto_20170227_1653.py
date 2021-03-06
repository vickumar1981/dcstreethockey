# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-02-27 21:53
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('leagues', '0003_auto_20170226_1434'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='league',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='leagues.League'),
        ),
        migrations.AddField(
            model_name='season',
            name='is_current_season',
            field=models.NullBooleanField(),
        ),
        migrations.AddField(
            model_name='season',
            name='season_type',
            field=models.PositiveIntegerField(choices=[(1, 'Spring'), (2, 'Summer'), (3, 'Fall'), (4, 'Winter')], null=True),
        ),
        migrations.AddField(
            model_name='season',
            name='year',
            field=models.CharField(max_length=4, null=True),
        ),
        migrations.AddField(
            model_name='stat',
            name='league',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='leagues.League'),
        ),
        migrations.AlterField(
            model_name='roster',
            name='position1',
            field=models.PositiveIntegerField(choices=[(1, 'Center'), (2, 'Wing'), (3, 'Defense'), (4, 'Goalie')]),
        ),
        migrations.AlterField(
            model_name='roster',
            name='position2',
            field=models.PositiveIntegerField(choices=[(1, 'Center'), (2, 'Wing'), (3, 'Defense'), (4, 'Goalie')]),
        ),
    ]
