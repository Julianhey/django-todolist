# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-09 02:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('list', '0004_gameinstance'),
    ]

    operations = [
        migrations.AddField(
            model_name='gameinstance',
            name='platform',
            field=models.CharField(default='Not specified', max_length=200),
        ),
    ]
