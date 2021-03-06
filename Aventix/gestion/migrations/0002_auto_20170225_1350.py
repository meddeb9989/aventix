# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-25 13:50
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('gestion', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='commercant',
            name='mdp',
        ),
        migrations.RemoveField(
            model_name='employe',
            name='mdp',
        ),
        migrations.RemoveField(
            model_name='employeur',
            name='mdp',
        ),
        migrations.AddField(
            model_name='commercant',
            name='user',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='employe',
            name='user',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='employeur',
            name='user',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
