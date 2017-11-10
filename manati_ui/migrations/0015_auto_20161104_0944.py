#
# Copyright (c) 2017 Stratosphere Laboratory.
# 
# This file is part of ManaTI Project 
# (see <https://stratosphereips.org>). It was created by 'Raul B. Netto <raulbeni@gmail.com>'
# 
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
# 
# You should have received a copy of the GNU Affero General Public License
# along with this program. See the file 'docs/LICENSE' or see <http://www.gnu.org/licenses/> 
# for copying permission.
#
# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-11-04 09:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manati_ui', '0014_moduleauxweblog'),
    ]

    operations = [
        migrations.AlterField(
            model_name='weblog',
            name='verdict',
            field=models.CharField(choices=[('malicious', 'Malicious'), ('legitimate', 'Legitimate'), ('suspicious', 'Suspicious'), ('undefined', 'Undefined'), ('falsepositive', 'False Positive'), ('malicious_legitimate', 'Malicious/Legitimate'), ('suspicious_legitimate', 'Suspicious/Legitimate'), ('undefined_legitimate', 'Undefined/Legitimate'), ('falsepositive_legitimate', 'False Positive/Legitimate'), ('undefined_malicious', 'Undefined/Malicious'), ('suspicious_malicious', 'Suspicious/Malicious'), ('falsepositive_malicious', 'False Positive/Malicious'), ('falsepositive_suspicious', 'False Positive/Suspicious'), ('undefined_suspicious', 'Undefined/Suspicious'), ('undefined_falsepositive', 'Undefined/False Positive')], default='undefined', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='webloghistory',
            name='old_verdict',
            field=models.CharField(choices=[('malicious', 'Malicious'), ('legitimate', 'Legitimate'), ('suspicious', 'Suspicious'), ('undefined', 'Undefined'), ('falsepositive', 'False Positive'), ('malicious_legitimate', 'Malicious/Legitimate'), ('suspicious_legitimate', 'Suspicious/Legitimate'), ('undefined_legitimate', 'Undefined/Legitimate'), ('falsepositive_legitimate', 'False Positive/Legitimate'), ('undefined_malicious', 'Undefined/Malicious'), ('suspicious_malicious', 'Suspicious/Malicious'), ('falsepositive_malicious', 'False Positive/Malicious'), ('falsepositive_suspicious', 'False Positive/Suspicious'), ('undefined_suspicious', 'Undefined/Suspicious'), ('undefined_falsepositive', 'Undefined/False Positive')], default='undefined', max_length=50),
        ),
        migrations.AlterField(
            model_name='webloghistory',
            name='verdict',
            field=models.CharField(choices=[('malicious', 'Malicious'), ('legitimate', 'Legitimate'), ('suspicious', 'Suspicious'), ('undefined', 'Undefined'), ('falsepositive', 'False Positive'), ('malicious_legitimate', 'Malicious/Legitimate'), ('suspicious_legitimate', 'Suspicious/Legitimate'), ('undefined_legitimate', 'Undefined/Legitimate'), ('falsepositive_legitimate', 'False Positive/Legitimate'), ('undefined_malicious', 'Undefined/Malicious'), ('suspicious_malicious', 'Suspicious/Malicious'), ('falsepositive_malicious', 'False Positive/Malicious'), ('falsepositive_suspicious', 'False Positive/Suspicious'), ('undefined_suspicious', 'Undefined/Suspicious'), ('undefined_falsepositive', 'Undefined/False Positive')], default='undefined', max_length=50),
        ),
    ]
