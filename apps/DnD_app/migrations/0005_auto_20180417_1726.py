# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-04-17 23:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DnD_app', '0004_auto_20180417_1725'),
    ]

    operations = [
        migrations.AlterField(
            model_name='character',
            name='image_route',
            field=models.CharField(default='img', max_length=255, null=True),
        ),
    ]
