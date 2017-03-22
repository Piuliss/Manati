# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-10-04 14:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manati_ui', '0011_vtconsult'),
    ]

    operations = [
        migrations.AddField(
            model_name='webloghistory',
            name='old_verdict',
            field=models.CharField(choices=[('malicious', 'Malicious'), ('legitimate', 'Legitimate'), ('suspicious', 'Suspicious'), ('undefined', 'Undefined'), ('false_positive', 'False Positive'), ('malicious_legitimate', 'Malicious/Legitimate'), ('suspicious_legitimate', 'Suspicious/Legitimate'), ('undefined_legitimate', 'Undefined/Legitimate'), ('false_positive_legitimate', 'False Positive/Legitimate'), ('undefined_malicious', 'Undefined/Malicious'), ('suspicious_malicious', 'Suspicious/Malicious'), ('false_positive_malicious', 'False Positive/Malicious'), ('false_positive_suspicious', 'False Positive/Suspicious'), ('undefined_suspicious', 'Undefined/Suspicious'), ('undefined_false_positive', 'Undefined/False Positive')], default='undefined', max_length=20),
        ),
    ]