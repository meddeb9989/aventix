# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-25 16:17
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gestion', '0005_auto_20170225_1616'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='carte',
            name='num',
        ),
    ]
