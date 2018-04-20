# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-04-20 19:18
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('DnD_app', '0006_auto_20180417_1726'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='character',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='character', to='DnD_app.Character'),
            preserve_default=False,
        ),
    ]
