# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-09-27 14:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manati_ui', '0008_auto_20160927_1243'),
    ]

    operations = [
        migrations.AlterField(
            model_name='metric',
            name='event_name',
            field=models.CharField(max_length=200),
        ),
    ]