# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-25 16:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestion', '0003_remove_carte_id_employe'),
    ]

    operations = [
        migrations.AddField(
            model_name='carte',
            name='num',
            field=models.IntegerField(default=0, max_length=16, unique=True),
            preserve_default=False,
        ),
    ]
